#!/usr/bin/env python3

import numpy as np
import imageio
import sys
from PIL import Image



############################## COMPUTE FIRST AND LAST LINE ###################
def getFirstLine(common):
    computedPrimera = []

    for el in common:
        newVal = (el+255)//2
        if newVal> (el+(255//2)+0.5):
            newVal+=1
        computedPrimera.append(newVal)
    
    return computedPrimera


############################## COMPUTE FIRST AND LAST LINE ###################



############################## READ #####################################

commonLine =[]

with open(sys.argv[1], "rb") as f:
    testReconstructed = []
    read = f.read()
    i=0
    cont=0
    ultimaRepetida = 100
    
    #header
    reconstructed_y = int.from_bytes(read[:3], byteorder="big")
    reconstructed_x = int.from_bytes(read[3:6], byteorder="big")

    leftMargin = int.from_bytes(read[6:9], byteorder="big")
    rightMargin = int.from_bytes(read[9:12], byteorder="big")
    margeInferior = int.from_bytes(read[12:15], byteorder="big")
    
    ultimaLinea = [255 for i in range(reconstructed_x)]
    
    read = read[15:]
    
    
    for j in range(reconstructed_x-12-12):
        commonLine.append(int.from_bytes(read[i:i+3], byteorder="big"))
        i+=3
    
    
    #ultima linea
    for j in range(12, leftMargin):
        ultimaLinea[j] = int.from_bytes(read[i:i+3], byteorder="big")
        i+=3
        
    
    for j in range(rightMargin, reconstructed_x):
        ultimaLinea[j] = int.from_bytes(read[i:i+3], byteorder="big")
        i+=3

############################## READ #####################################


############################## RECONSTRUCTION ###########################


#12 first 255
finalReconstructed = [255 for x in range(12)]

#12 last 255
for i in range(12):
    commonLine.append(255)

    
finalReconstructed += commonLine



primera = getFirstLine(finalReconstructed)

img_reconstructed = np.array([[255 for x in range(reconstructed_x)] for j in range(reconstructed_y)])

#asignem la primera fila
img_reconstructed[12] = primera
img_reconstructed[13:ultimaRepetida] = finalReconstructed
print(img_reconstructed)



#laterals:

#LEFT
for i in range(ultimaRepetida, margeInferior):
    for j in range(leftMargin):
        img_reconstructed[i][j] = finalReconstructed[j]

#RIGHT
for i in range(ultimaRepetida, margeInferior):
    for j in reversed(range(rightMargin, reconstructed_x)):
        img_reconstructed[i][j] = finalReconstructed[j]

        
#Last Line
for j in range(12, leftMargin):
    img_reconstructed[margeInferior][j] = ultimaLinea[j]

for j in reversed(range(rightMargin, reconstructed_x-12)):
    img_reconstructed[margeInferior][j] = ultimaLinea[j]

############################## RECONSTRUCTION ###########################


############################## SAVE IMAGE ###############################


img_reconstructed = img_reconstructed.astype(dtype=np.uint8)

imgToSave = Image.fromarray(img_reconstructed)
imgToSave.save(sys.argv[2])
print("Imatge", sys.argv[2], "creada")


############################## SAVE IMAGE ###############################

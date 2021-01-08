#!/usr/bin/env python3

import numpy as np
import imageio
import sys
from PIL import Image


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
    
    
    read = read[6:]
    
    
    for j in range(len(test)):
    
        commonLine.append(int.from_bytes(read[i:i+3], byteorder="big"))
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
ultima = getLastLine(finalReconstructed)


img_reconstructed = np.array([[255 for x in range(shape_x)] for j in range(shape_y)])

#asignem la primera fila
img_reconstructed[12] = primera
img_reconstructed[12:ultimaRepetida] = finalReconstructed
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
    img_reconstructed[margeInferior][j] = ultima[j]

for j in reversed(range(rightMargin, reconstructed_x-12)):
    img_reconstructed[margeInferior][j] = ultima[j]

############################## RECONSTRUCTION ###########################


############################## SAVE IMAGE ###############################

imgToSave = Image.fromarray(img_reconstructed, "RGB")
imgToSave.save(sys.argv[2])
print("Imatge", sys.argv[2], "creada")


############################## SAVE IMAGE ###############################

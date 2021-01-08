#!/usr/bin/env python3

import numpy as np
import imageio
import sys


img = imageio.imread(sys.argv[1])
plt.imshow(img) #im


############################## FIND ENDS #####################################
primeraLinea = 0
segonaLinea = 0
ultimaRepetida = 0
margeInferior = 0

for fila in range(img.shape[0]):
    for columna in range(img.shape[1]):
        if img[fila][columna] != 255:
            if primeraLinea == 0:
                primeraLinea = fila
                segonaLinea = fila+1


segonaLinea = img[segonaLinea]

for x in range(primeraLinea+1, img.shape[0]):
    
    if False in (img[x] == segonaLinea):
        if ultimaRepetida == 0:
            ultimaRepetida = x


for i in range(img.shape[0]):
    if img[i][12] != 255:
        margeInferior = i


            
#Left Margin
leftMargin = 0
           
for i in range(len(img[ultimaRepetida])):
    if img[ultimaRepetida-1][i] != img[ultimaRepetida][i]:
        if leftMargin ==0:
            leftMargin = i

            
            
#Right Margin
rightMargin = 0

for i in reversed(range(len(img[ultimaRepetida]))):
    if img[ultimaRepetida-1][i] != img[ultimaRepetida][i]:
        if rightMargin ==0:
            rightMargin = i
            
            
############################## FIND ENDS #####################################




############################## COMPUTE FIRST AND LAST LINE ###################
def getFirstLine(common):
    computedPrimera = []

    for el in common:
        newVal = (el+255)//2
        if newVal> (el+(255//2)+0.5):
            newVal+=1
        computedPrimera.append(newVal)
    
    return computedPrimera


def getLastLine(common):
    computedLast = []

    for el in common:
        if el != 255:
            newVal = (el+255)//1.77
            if newVal> (el+(255//1.77)+0.5):
                newVal+=1
        else:
            newVal = 255
        computedLast.append(newVal)
            
    return computedLast

############################## COMPUTE FIRST AND LAST LINE ###################




############################## WRITE #####################################

shape_x = img.shape[1]
shape_y = img.shape[0]

test1 = np.asarray(img[13]) #common row
test1 = test1.tolist()


#remove first and last 12 255
test = test1[12:-12]


#write
with open(sys.argv[2], "wb+") as f:
    
    #header
    f.write(shape_y.to_bytes(3, byteorder="big", signed=False))
    f.write(shape_x.to_bytes(3, byteorder="big", signed=False))
    
    
    for i in range(len(test)):
        f.write(test[i].to_bytes(3, byteorder="big", signed=False))

############################## WRITE #####################################





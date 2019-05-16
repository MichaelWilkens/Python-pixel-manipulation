import sys
import cv2
import numpy as np
import matplotlib.pyplot as plt

# import image from file, and save it as an array
image = cv2.imread("black.jpg")
arrayImage = np.asarray(image)

finalImage = []

#row building functions
def buildWhiteRow():
    whiteRow = []
    for x in range(0, len(arrayImage[0])):
        whiteRow.append([250,250,250])
    return finalImage.append(whiteRow)

def buildStripedRow():
    stripedRow = []
    for x in range(0, len(arrayImage[0])):
        if (x >= 1499 and x <= 1749) or (x >= 2499 and x <= 2749):
            stripedRow.append([250, 250, 250])               
        else:
            stripedRow.append([0,0,0])
    return finalImage.append(stripedRow)        

#matrix building function
def buildPattern():
    for y in range(0, len(arrayImage)):
        if (y >= 999 and y <= 1249) or (y >= 1999 and y <= 2249):
            buildWhiteRow()
        else:
            buildStripedRow()
    return         

#instantiate matrix function and pyplot
buildPattern()
plt.imshow(finalImage)
plt.show()    
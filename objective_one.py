import sys
import cv2
import numpy as np
import matplotlib.pyplot as plt

#import image from file, and save it as an array
image = cv2.imread("pattern.jpg")
arrayImage = np.asarray(image)

#initiate black pixel array and matrices
blackImage = []
blackRow = []

#builder functions
def buildBlackRow():
    for i in arrayImage[0]:
        blackRow.append([0,0,0])

def buildBlackImage():
    for i in arrayImage:
        blackImage.append(blackRow)

buildBlackRow()        
buildBlackImage()

#instantiate pyplot
plt.imshow(blackImage)
plt.show()
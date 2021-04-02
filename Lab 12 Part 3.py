#This program blends two images together, this can be used for opacity aplications and crossfading features. you could potentialy even crossfade video feeds.
import cv2 as cv
import numpy as np
import sys

#These images must be the same size
img1 = cv.imread('download.jpeg')                           #Selects an image file      
img2 = cv.imread('download1.jpeg')                          #Selects an image file

alpha = 0.2                                                 #Sets the alpha weight for the crossfading thickness
dst = cv.addWeighted(img1, alpha, img2, 1-alpha, 0.0)       #sets the crossfade perameters for the selescted images
cv.imshow('dst', dst)                                       #shows the newly created image with the two crossfadded images
cv.waitKey(0)                                               #Waits untill key is pressed
cv.destroyAllWindows                                        #Destroys the windows
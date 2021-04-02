import cv2 as cv
import sys

img = cv.imread('dragon2.png')                    #Selects the file to be used
img = cv.resize(img,None,fx=3, fy=3, interpolation = cv.INTER_CUBIC)      #This resized the window
if img is None:                                   #Checks if there is a file
    sys.exit("The image could not be read.")      #Closes the window
cv.imshow("OpenCV Image", img)                    #Shows the image with the title given

cv.waitKey(0)                                     #Waits untill a key is pressed
cv.destroyAllWindows()                            #closed the window
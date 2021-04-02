#This program removes all colour and depth of the image and changes it to just show the outline and/or detailing
#This program would be good in aplications where you only need to see positioning or orientation or an image

import cv2 as cv
import numpy as np

#img = cv.imread('dragon.jpeg')                                       #selects an image to be oulined
#res = cv.resize(img,None,fx=3,fy=3,interpolation=cv.INTER_CUBIC)     #Resized the image
cap = cv.VideoCapture(0)
if not cap.isOpened:
    print("Cannot open Camera")
    exit()
while True:
    ret, frame = cap.read()
    # if frame is read correctly ret is true
    if not ret:
        print("Cant recieve frame (Stream end?). Exiting...")
        break
 
    cv.imwrite("canny.jpg", cv.Canny(frame, 200, 300)) #Canny in one line
    cv.imshow("canny", cv.imread("canny.jpg"))                           #shows the outlined image
    if cv.waitKey(1) == ord('q'):
        break
    
#When everything is done release the capture
cap.release()
cv.destroyAllWindows()
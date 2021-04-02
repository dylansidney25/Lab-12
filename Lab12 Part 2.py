#This program opens up a live video window in either color or monochrome. This code could be used in streaming aplications like security or televison.
import numpy as np
import cv2 as cv
cap = cv.VideoCapture(0)
if not cap.isOpened:
    print("Cannot open Camera")
    exit()
while True:
    # Capture frame by frame
    ret, frame = cap.read()
    # if frame is read correctly ret is true
    if not ret:
        print("Cant recieve frame (Stream end?). Exiting...")
        break
    #Our operations on the frame come here
    grey = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    
    #Display the resulting frame
    cv.imshow('frame', grey)
    #cv.imshow('frame', frame)
    
    if cv.waitKey(1) == ord('q'):
        break
#When everything is done release the capture
cap.release()
cv.destroyAllWindows()
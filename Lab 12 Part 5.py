#This program shows the image files in two variants. one image is over lined with the lines highlightd and the other is shown as just the lines.
import cv2 as cv
import numpy as np


img = cv.imread('Lines.jpeg')             #This line selects the image from the same directory the file is located in

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)  #Creates another image of the origonal just using grey colors
edges = cv.Canny(gray, 50, 120)             #Creates a line only version of the image grey
minLineLength = 20
maxLineGap = 5

lines = cv.HoughLinesP(edges, 1, np.pi/180.0, 20, minLineLength, maxLineGap)
No_lines,a,b = np.shape(lines)

print(No_lines)
for index in range(No_lines):
   
    for x1, y1, x2, y2 in lines[index]:
        cv.line(img, (x1, y1), (x2, y2), (0,255,0),2)
        cv.imshow("edges", edges)
        cv.imshow("lines", img)

cv.waitKey()
cv.destroyAllWindows()
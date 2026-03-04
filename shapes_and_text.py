import cv2 as cv 
import numpy as np


input_text = input("enter text to display")
def rescale(frame, scale=0.2):
    w = int(frame.shape[1] * scale)
    h = int(frame.shape[0] * scale)
    return cv.resize(frame, (w, h), interpolation=cv.INTER_AREA)

img = cv.imread("C:\\Users\\harsh\\Pictures\\cams\\101_0119.JPG")
img = rescale(img)
cv.imshow("bike",img)

#rectangle
cv. rectangle(img, (0,0), (225,225), (0,0,225),thickness= 3)
cv.imshow("rect",img)

#circle
cv.circle(img, (225,225),40, (0,0,225),thickness= 3 )
cv.imshow("circle", img)

#line 
cv.line(img,(0,0), (225,225), (0,0,225),thickness= 3 )
cv.imshow("line",img)

#write text
cv.putText(img, input_text,(225,255), cv.FONT_HERSHEY_COMPLEX_SMALL, 1.0, (255,0,0), 3)
cv.imshow("text in img", img)
cv.waitKey(0)

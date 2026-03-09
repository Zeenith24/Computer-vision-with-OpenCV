import cv2 as cv
import numpy as np 

def rescale(frame, scale=0.2):
    w = int(frame.shape[1] * scale)
    h = int(frame.shape[0] * scale)
    return cv.resize(frame, (w, h), interpolation=cv.INTER_AREA)

img = cv.imread("C:\\Users\\harsh\\Pictures\\cams\\101_0119.JPG")
img = rescale(img)
cv.imshow("bike",img)

grey = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
canny = cv.Canny(img, 125, 175)
cv.imshow("canny", canny)

contours , heirarcy = cv.findContours(canny , cv.RETR_LIST, cv.CHAIN_APPROX_NONE )
print(f"{len(contours)} contour(s) found")
cv.waitKey(0) 
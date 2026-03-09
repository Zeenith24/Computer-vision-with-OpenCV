import cv2 as cv 
import numpy as np 
import matplotlib.pyplot as plt 


def rescale(frame, scale=0.2):
    w = int(frame.shape[1] * scale)
    h = int(frame.shape[0] * scale)
    return cv.resize(frame, (w, h), interpolation=cv.INTER_AREA)

img = cv.imread("C:\\Users\\harsh\\Pictures\\cams\\101_0119.JPG")
img = rescale(img)
cv.imshow("bike",img)


# BGR TO HSV 
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow("hsv", hsv)

# BGR to L*a*b
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow("lab", lab)

# BGR to RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow("rgb",rgb)

plt.imshow(rgb)
plt.show()
cv.waitKey(0)
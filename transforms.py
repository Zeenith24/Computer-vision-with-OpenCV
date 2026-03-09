import cv2 as cv 
import numpy as np

def rescale(frame, scale=0.2):
    w = int(frame.shape[1] * scale)
    h = int(frame.shape[0] * scale)
    return cv.resize(frame, (w, h), interpolation=cv.INTER_AREA)

img = cv.imread("C:\\Users\\harsh\\Pictures\\cams\\101_0119.JPG")
img = rescale(img)
cv.imshow("bike",img)

#translation function
def translate(img , x, y):
    transmat = np.float32([[1,0,x],[0,1,y]])
    dims = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transmat,dims)

# -x --> left , -y --> up
# +x --> right , +y --> down
translated = translate(img, 100, 100)
cv.imshow("trans", translated)

cv.waitKey(0)

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
# cv.imshow("trans", translated)

#rotate 
def rotate ( img , angle, rotpoint = None):
    (height, width) = img.shape[:2]

    if rotpoint is None :
        rotpoint = (width//2, height//2)

    rotMat = cv.getRotationMatrix2D(rotpoint, angle, 1.0)
    dims = (width, height)

    return cv.warpAffine(img , rotMat, dims)

roated = rotate(img, 90)
# cv.imshow("roated", roated)

#resizing 
resize  = cv.resize(img , (500, 500), interpolation=cv.INTER_LINEAR)
# cv.imshow("resized", resize)

#fliping 
# 0 --> vertically, 1--> horizontally , -1 --> both 
flip = cv.flip(img, -1)
# cv.imshow("flip", flip)

#cropping 
crop = img[200:400, 300:400]
cv.imshow("crop", crop)

cv.waitKey(0)

import cv2 as cv 

def rescale(frame, scale=0.2):
    w = int(frame.shape[1] * scale)
    h = int(frame.shape[0] * scale)
    return cv.resize(frame, (w, h), interpolation=cv.INTER_AREA)

img = cv.imread("C:\\Users\\harsh\\Pictures\\cams\\101_0119.JPG")
img = rescale(img)
# cv.imshow("bike",img)

# convert to greyscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow("grayscale", gray)

#blur image
blur = cv.GaussianBlur(img, (3,3), cv.BORDER_DEFAULT)
# cv.imshow("blur", blur)

#edge cascade
canny = cv.Canny(img, 125, 175)
# cv.imshow("canny", canny)

#dailating image
dialated = cv.dilate(canny, (7,7), iterations=3)
# cv.imshow("dialated", dialated)

#eroding 
erode = cv.erode(dialated, (7,7), iterations= 3)
# cv.imshow("erode", erode)

#resize 
resize = cv.resize(img, (500,500))
cv.imshow("resize", resize)

#crop
cropped = img[50:200, 200:400]
cv.imshow("cropped", cropped)
cv.waitKey(0)
import cv2 as cv



def rescale(frame, scale = 0.75):
    # works for images, videos and live vids
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dims = (width, height)

    return cv.resize(frame, dims, interpolation=cv.INTER_AREA) 

capture = cv.VideoCapture("C:\\Users\\harsh\\Pictures\\cams\\101_0177.MOV")
while True:
    isTrue, frame = capture.read()

    frame_resize = rescale(frame)
    cv.imshow('video', frame)
    cv.imshow("video resized", frame_resize)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

def change_res(width, height):
    # works only for live vids 
    capture.set(3, width)
    capture.set(4, height)

capture.release()
cv.destroyAllWindows()
cv.waitKey(0)
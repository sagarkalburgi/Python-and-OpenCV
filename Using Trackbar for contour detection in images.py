# Using Trackbar for contour detection in images

import cv2

def nothing(x):
    pass

img = cv2.imread('circles.jpg')

cv2.imshow('image',img)

cv2.createTrackbar('thr', 'image', 1,255, nothing)

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

while True:
    cv2.imshow('image', img)
    
    thr = cv2.getTrackbarPos('thr', 'image')
    
    ret,thr1 = cv2.threshold(img_gray, thr, 255, cv2.THRESH_BINARY)
    
    contours,_ = cv2.findContours(thr1, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    
    cv2.drawContours(img, contours, -1, (0,255,0), 2)
    cv2.imshow('image', img)
    cv2.imshow('gray', thr1)
    if cv2.waitKey(1) == ord('q'):
        break
    
cv2.destroyAllWindows()
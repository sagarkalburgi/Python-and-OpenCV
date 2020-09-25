# Using trackbars for various morphological operations on videos

import cv2
import numpy as np

def nothing(x):
    pass
    
cap = cv2.VideoCapture('kitten playing.mp4')
ret, img = cap.read()
cv2.imshow('image', img)

cv2.createTrackbar('Thr', 'image', 0,255, nothing)
cv2.createTrackbar('kernel', 'image', 1,10, nothing)
cv2.createTrackbar('iter', 'image', 1,10, nothing)

while cap.isOpened():
    ret, img = cap.read()
    if cv2.waitKey(1) == ord('q') or ret == False:
        break
    cv2.imshow('image', img)
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    thr = cv2.getTrackbarPos('Thr','image') 
  
    _,thr1 = cv2.threshold(gray_img, thr, 255, cv2.THRESH_BINARY )

    pix = cv2.getTrackbarPos('kernel','image')
    iters = cv2.getTrackbarPos('iter','image')
    kernel = np.ones((pix,pix), np.uint8)
    
    dilation = cv2.dilate(thr1, kernel, iterations=iters)
    erode = cv2.erode(thr1, kernel, iterations=iters)
    opening = cv2.morphologyEx(thr1, cv2.MORPH_OPEN, kernel)
    closing = cv2.morphologyEx(thr1, cv2.MORPH_CLOSE, kernel)

    cv2.imshow('Dilation', dilation)
    cv2.imshow('Erosion', erode)
    cv2.imshow('Opening', opening)
    cv2.imshow('Closing', closing)

cap.release()
cv2.destroyAllWindows()
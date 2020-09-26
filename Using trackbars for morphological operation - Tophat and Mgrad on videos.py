# Using trackbars for morphological operation - Tophat and Mgrad on videos

import cv2
import numpy as np

def nothing(x):
    pass

cap = cv2.VideoCapture('kitten playing.mp4')
ret, img = cap.read()
cv2.imshow('image', img)

cv2.createTrackbar('Thr', 'image', 0,255, nothing)
cv2.createTrackbar('kernel', 'image', 1,10, nothing)

while cap.isOpened():
    ret, img = cap.read()
    if cv2.waitKey(1) == ord('q') or ret == False:
        break
    cv2.imshow('image', img)

    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    thr = cv2.getTrackbarPos('Thr','image') 
    pix = cv2.getTrackbarPos('kernel','image')
    
    _,thr1 = cv2.threshold(gray_img, thr, 255, cv2.THRESH_BINARY )
    kernel = np.ones((pix,pix), np.uint8)
    
    mgrad = cv2.morphologyEx(thr1, cv2.MORPH_GRADIENT, kernel)
    tophat = cv2.morphologyEx(thr1, cv2.MORPH_TOPHAT, kernel)

    cv2.imshow('Mgrad', mgrad)
    cv2.imshow('Tophat', tophat)

cap.release()
cv2.destroyAllWindows()
# Using trackbars for morphological operation-thresholding on videos

import cv2

def nothing(x):
    pass
    
cap = cv2.VideoCapture('kitten playing.mp4')
ret, img = cap.read()
cv2.imshow('image', img)

cv2.createTrackbar('Thr', 'image', 0,255, nothing)
cv2.createTrackbar('Thr_mean', 'image', 11,50, nothing)
cv2.createTrackbar('Thr_gaus', 'image', 11,50, nothing)
cv2.createTrackbar('Thr_c', 'image', 1,10, nothing)

while cap.isOpened():
    ret, img = cap.read()
    if cv2.waitKey(1) == ord('q') or ret == False:
        break
    cv2.imshow('image', img)
    
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    thr = cv2.getTrackbarPos('Thr','image') 
    thr_mean = cv2.getTrackbarPos('Thr_mean','image') 
    thr_gaus = cv2.getTrackbarPos('Thr_gaus','image') 
    thr_c = cv2.getTrackbarPos('Thr_c','image') 
    
    _,thr1 = cv2.threshold(gray_img, thr, 255, cv2.THRESH_BINARY )
    if (thr_mean % 2) == 1 and thr_mean > 2:
        thr2 = cv2.adaptiveThreshold(gray_img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, thr_mean, thr_c)
    if (thr_gaus % 2) == 1 and thr_gaus > 2:
        thr3 = cv2.adaptiveThreshold(gray_img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, thr_gaus, thr_c)

    cv2.imshow('Thresh', thr1)
    cv2.imshow('Thresh Mean', thr2)
    cv2.imshow('Thresh Gaus', thr3)

cap.release()
cv2.destroyAllWindows()
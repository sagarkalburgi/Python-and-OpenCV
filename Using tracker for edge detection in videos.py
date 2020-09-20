# Using tracker for edge detection in videos

import cv2
import numpy as np

def nothing(x):
    pass

img = np.zeros([100,500,3], np.uint8)
cv2.imshow('image',img)

cv2.createTrackbar('thr1', 'image', 1,200, nothing)
cv2.createTrackbar('thr2', 'image', 1,200, nothing)
cv2.createTrackbar('sobel', 'image', 0,1, nothing)

cap = cv2.VideoCapture('Wolf.mp4')

while cap.isOpened():
    ret, img = cap.read()
    if cv2.waitKey(1) == ord('q') or ret == False:
        break
    cv2.imshow('image',img)
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    sobel = cv2.getTrackbarPos('sobel', 'image')
    thr1 = cv2.getTrackbarPos('thr1', 'image')
    thr2 = cv2.getTrackbarPos('thr2', 'image')
        
    sobelx = cv2.Sobel(gray_img, cv2.CV_64F, 1,0)
    sobelx = np.uint8(np.absolute(sobelx))
    cv2.imshow('Sobel X', sobelx)
    
    sobely = cv2.Sobel(gray_img, cv2.CV_64F, 0,1)
    sobely = np.uint8(np.absolute(sobely))
    cv2.imshow('Sobel Y', sobely)
    
    if sobel == 1:   
        sobel_com = cv2.bitwise_or(sobelx, sobely)
        cv2.imshow('Sobel Combined', sobel_com)
    
    if thr1 > 1:
        canny = cv2.Canny(gray_img, thr1, thr2)
        cv2.imshow('Canny', canny)
    
cap.release()
cv2.destroyAllWindows()
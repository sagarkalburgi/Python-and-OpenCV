# Using Trackbars for smoothening and blurring operations on videos

import cv2
import numpy as np

def nothing(x):
    pass

img = np.zeros([100,500,3], np.uint8)
cv2.imshow('image',img)

cv2.createTrackbar('pix', 'image', 1,20, nothing)
cv2.createTrackbar('sigma_color', 'image', 1,200, nothing)
cv2.createTrackbar('sigma_space', 'image', 1,200, nothing)

cap = cv2.VideoCapture('kitten playing.mp4')

while cap.isOpened:
    ret, img = cap.read()
    
    if cv2.waitKey(1) == ord('q') or ret == False:
        break
    
    cv2.imshow('image', img)
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    pix = cv2.getTrackbarPos('pix', 'image')
    sigma_color = cv2.getTrackbarPos('sigma_color', 'image')
    sigma_space = cv2.getTrackbarPos('sigma_space', 'image')
    
    if pix >= 1:
        kernel = np.ones((pix,pix), np.float32)/(pix*pix)
    
        dst = cv2.filter2D(img, -1, kernel)
    
        blur = cv2.blur(img, (pix,pix))
        
        bilateral = cv2.bilateralFilter(img, pix, sigma_color, sigma_space)
    
    if (pix % 2) == 1 and pix > 2:
        gaus_blur = cv2.GaussianBlur(img, (pix,pix), 0)
        median = cv2.medianBlur(img, pix)
        cv2.imshow('Gaussian Blur', gaus_blur)
        cv2.imshow('Median Blur', median)
    
    cv2.imshow('Bilateral', bilateral)  
    cv2.imshow('2D Convolution', dst)
    cv2.imshow('Blur', blur)
    
cap.release()
cv2.destroyAllWindows()
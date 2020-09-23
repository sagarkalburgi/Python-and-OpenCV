# Using trackbars for morphological operations-masking on images

import cv2
import numpy as np

def nothing(x):
    pass

img = cv2.imread('cycling.jfif')
cv2.imshow('image', img)

cv2.createTrackbar('LH', 'image', 0,255, nothing)
cv2.createTrackbar('LS', 'image', 0,255, nothing)
cv2.createTrackbar('LV', 'image', 0,255, nothing)

while True:
    if cv2.waitKey(1) == ord('q'):
        break
    hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    lh = cv2.getTrackbarPos('LH','image')        
    ls = cv2.getTrackbarPos('LS','image')        
    lv = cv2.getTrackbarPos('LV','image')   
    low_bound = np.array([lh,ls,lv])
    upp_bound = np.array([255,255,255])
    
    mask = cv2.inRange(hsv_img, low_bound, upp_bound)
    res = cv2.bitwise_and(img, img, mask = mask)

    cv2.imshow('mask', mask)
    cv2.imshow('res', res)

cv2.destroyAllWindows()
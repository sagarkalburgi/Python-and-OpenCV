# Green color masking using images

import cv2
import numpy as np

cap = cv2.VideoCapture('green_mask.mp4')

img = cv2.imread('cat.jfif')

while cap.isOpened():
    ret ,frame = cap.read()
    if cv2.waitKey(1) == ord('q') or ret == False:
        break
    
    frame = cv2.resize(frame, (500,500), interpolation = cv2.INTER_AREA)
    frame = cv2.bilateralFilter(frame, 9, 75, 75)
    
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    lower_green = np.array([45,100,50])
    upper_green = np.array([75,255,255])

    mask = cv2.inRange(hsv, lower_green, upper_green)
    mask_inv = cv2.bitwise_not(mask)
    
    img_masked = cv2.bitwise_and(img, img, mask=mask)
    frame_masked = cv2.bitwise_and(frame, frame, mask=mask)
    frame_masked_inv = cv2.bitwise_and(frame, frame, mask= mask_inv)
    
    final_res = cv2.add(img_masked, frame_masked_inv)
    
    gray = cv2.cvtColor(frame_masked, cv2.COLOR_BGR2GRAY)
    
    _,thr = cv2.threshold(gray, 100, 255, 0)
    contours,_ = cv2.findContours(thr, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    cv2.imshow('img', img)
    cv2.imshow('Original_frame', frame)
    cv2.imshow('Frame_masked_inv', frame_masked_inv)
    cv2.imshow("Img_masked", img_masked)
    cv2.imshow("Final_Image", final_res)
    
cap.release() 
cv2.destroyAllWindows()
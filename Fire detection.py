# Fire detection

import cv2
import numpy as np

cap = cv2.VideoCapture('fire.mp4')

while cap.isOpened():
    ret ,frame = cap.read()
    if cv2.waitKey(1) == ord('q') or ret == False:
        break
    
    frame = cv2.bilateralFilter(frame, 9, 75, 75)
    
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    l_bound = np.array([0,50,50])
    u_bound = np.array([35,255,255])
    
    mask = cv2.inRange(hsv, l_bound, u_bound)
    
    res = cv2.bitwise_and(frame, frame, mask= mask)
    res_con = cv2.bitwise_and(frame, frame, mask= mask)
    
    gray = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)
    canny = cv2.Canny(gray, 100, 200)
    
    _,thr = cv2.threshold(mask, 100, 255, 0)
    contours,_ = cv2.findContours(thr, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    cv2.drawContours(res_con, contours, -1, (255,0,0), 3)

    cv2.imshow('Original Frame', frame)
    cv2.imshow('Mask', mask)
    cv2.imshow('Res', res)
    cv2.imshow('Res_con', res_con)
    cv2.imshow('canny', canny)

cap.release() 
cv2.destroyAllWindows()
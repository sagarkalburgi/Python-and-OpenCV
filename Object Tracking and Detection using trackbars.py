# Object Tracking and Detection using trackbars

import cv2
import numpy as np

def nothing(x):
    pass

cap = cv2.VideoCapture('kitten playing.mp4')
ret, frame = cap.read()
cv2.imshow('Tracking', frame)
cv2.createTrackbar('LH', 'Tracking', 0, 255, nothing)
cv2.createTrackbar('LS', 'Tracking', 0, 255, nothing)
cv2.createTrackbar('LV', 'Tracking', 0, 255, nothing)
cv2.createTrackbar('T1', 'Tracking', 1, 300, nothing)
cv2.createTrackbar('T2', 'Tracking', 1, 300, nothing)

while cap.isOpened():
    ret,frame = cap.read()
    if cv2.waitKey(1) == ord('q') or ret == False:
        break
    
    frame = cv2.bilateralFilter(frame, 9, 75, 75)
    
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    l_hue = cv2.getTrackbarPos('LH', 'Tracking')
    l_saturation = cv2.getTrackbarPos('LS', 'Tracking')
    l_value = cv2.getTrackbarPos('LV', 'Tracking')
    
    u_hue = 255
    u_saturation = 255
    u_value = 255
    
    l_blue = np.array([l_hue,l_saturation,l_value])
    u_blue = np.array([u_hue,u_saturation,u_value])
    
    mask = cv2.inRange(hsv, l_blue, u_blue)
    
    res = cv2.bitwise_and(frame, frame, mask= mask)
    res_con = cv2.bitwise_and(frame, frame, mask= mask)
    
    T1 = cv2.getTrackbarPos('T1', 'Tracking')
    T2 = cv2.getTrackbarPos('T2', 'Tracking')
    
    gray = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)
    canny = cv2.Canny(gray, T1, T2)
    
    _,thr = cv2.threshold(gray, T1, 255, 0)
    contours,_ = cv2.findContours(thr, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    cv2.drawContours(res_con, contours, -1, (255,0,0), 3)
    
    cv2.imshow('Tracking', frame)
    cv2.imshow('Mask', mask)
    cv2.imshow('Res', res)
    cv2.imshow('Res_con', res_con)
    cv2.imshow('canny', canny)
    
cap.release() 
cv2.destroyAllWindows()
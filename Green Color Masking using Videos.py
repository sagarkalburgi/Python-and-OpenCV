# Green color masking using Videos

import cv2
import numpy as np

cap = cv2.VideoCapture('green_mask1.mp4')
cap2 = cv2.VideoCapture('wolf.mp4')

while True:
    ret1 ,frame = cap.read()
    ret2 ,img = cap2.read()
    if cv2.waitKey(1) == ord('q') or ret1 == False or ret2 == False:
        break
    
    frame = cv2.resize(frame, (640,360), interpolation = cv2.INTER_AREA)
    frame = cv2.bilateralFilter(frame, 9, 75, 75)
    
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    lower_green = np.array([45,100,100])
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
    
    cv2.imshow('Frame 2', img)
    cv2.imshow('Original_frame', frame)
    cv2.imshow('Frame_masked_inv', frame_masked_inv)
    cv2.imshow("Img_masked", img_masked)
    cv2.imshow("Final_Image", final_res)
    
cap.release() 
cv2.destroyAllWindows()
# Using Trackbar for contour detection in videos

import cv2

def nothing(x):
    pass

cap = cv2.VideoCapture('kitten playing.mp4')

ret, img = cap.read()

cv2.imshow('image',img)

cv2.createTrackbar('thr', 'image', 1,255, nothing)

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

while cap.isOpened():
    cv2.imshow('image', img)
    
    thr = cv2.getTrackbarPos('thr', 'image')
    
    ret,thr1 = cv2.threshold(img_gray, thr, 255, 0)
    
    contours,_ = cv2.findContours(thr1, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    
    cv2.drawContours(img, contours, -1, (0,255,0), 2)
    cv2.imshow('image', img)
    cv2.imshow('gray', thr1)
    
    ret, img = cap.read()
    if cv2.waitKey(1) == ord('q') or ret == False:
        break
    
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
cap.release()
cv2.destroyAllWindows()
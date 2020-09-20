# Background Subtractor

import cv2

cap = cv2.VideoCapture('kitten playing.mp4')

font = cv2.FONT_HERSHEY_COMPLEX

foreground_background_MOG = cv2.createBackgroundSubtractorMOG2(detectShadows=False)
foreground_background_KNN = cv2.createBackgroundSubtractorKNN(detectShadows=False)

while cap.isOpened():
    _,frame = cap.read()
    if frame is None:
        break
    
    foreground_mask_MOG = foreground_background_MOG.apply(frame)
    foreground_mask_KNN = foreground_background_KNN.apply(frame)
    
    foreground_mask_MOG = cv2.putText(foreground_mask_MOG, 'Background Subtractor MOG', (10,30), font, 1, (255,0,0), 2, cv2.LINE_AA)
    foreground_mask_KNN = cv2.putText(foreground_mask_KNN, 'Background Subtractor KNN', (10,30), font, 1, (255,0,0), 2, cv2.LINE_AA)

    cv2.imshow('frame', frame)
    cv2.imshow('Background Subtractor MOG', foreground_mask_MOG)
    cv2.imshow('Background Subtractor KNN', foreground_mask_KNN)
    
    if cv2.waitKey(1) == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()
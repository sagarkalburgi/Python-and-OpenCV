# Displaying date and time over videos using click_event

import cv2
import datetime

def click_event(event, x,y, flags, param):
    global ret
    if event == cv2.EVENT_LBUTTONDOWN:
        while cap.isOpened():
            ret, frame = cap.read()
            if cv2.waitKey(1) == ord('q') or ret == False:
                ret = False
                return 
            font = cv2.FONT_HERSHEY_COMPLEX
            date_time = datetime.datetime.now()
            text = date_time.strftime("Date: %d/%m/%Y Time-%H:%M:%S")
            frame = cv2.putText(frame, text, (x,y), font, 1, (255,0,0), 2, cv2.LINE_AA)
            cv2.imshow('Camera', frame)

cap = cv2.VideoCapture('wolf.mp4')
ret, frame = cap.read()
while cap.isOpened():
    ret, frame = cap.read()
    if cv2.waitKey(1) == ord('q') or ret == False:
        break
    cv2.imshow('Camera', frame)
    cv2.setMouseCallback('Camera', click_event)
    
cap.release()
cv2.destroyAllWindows()
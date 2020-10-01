# Cam shift object tracking using mouse click events
'''
This program uses two mouse click events by the user to track the object

First: Left mouse button to define the x, y of the object being tracked

Second: Right mouse button to define the x+w, y+h of the object

Then close the frame/window and the program shall track the object using cam shift method
'''
import cv2
import numpy as np

def click_event(event,x,y,flags,param):
    global a,b,c,d,n
    if event == cv2.EVENT_LBUTTONDOWN:          # Left click for x, y
        a = x
        b = y
        print(x,y)
    
    if event == cv2.EVENT_RBUTTONDOWN:          # Right click for x+w, y+h
        c = x
        d = y
        print(x,y)
        
def cam_shit():
    global frame,a,b,c,d
    cap = cv2.VideoCapture('traffic6.mp4')
    ret,frame = cap.read()
    if NameError == True:
        return
    x,y,w,h = a,b,c-a,d-b
    print(x,y,w,h)
    track_window = (x,y,w,h)
    
    roi = frame[y:y+h, x:x+w]
    hsv_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv_roi, np.array((0,60,31)), np.array((180,255,255)))
    roi_hist = cv2.calcHist([hsv_roi], [0], mask, [150], [0,180])
    cv2.normalize(roi_hist, roi_hist, 0, 255, cv2.NORM_MINMAX)
    term_crit = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1)
    
    while True:
        ret, frame = cap.read()
        if ret == True:
            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            dst = cv2.calcBackProject([hsv], [0], roi_hist, [0,180], 1)
            
            ret,track_window = cv2.CamShift(dst, track_window, term_crit)
            
            pts = cv2.boxPoints(ret)
            pts = np.int0(pts)
            final_img = cv2.polylines(frame, [pts], True, (255,0,0), 3)
            cv2.imshow('Final Image', final_img)
            if cv2.waitKey(1) == ord('q'):
                break
        else:
            break
    cap.release()
    cv2.destroyAllWindows()
    return

cap = cv2.VideoCapture('traffic6.mp4')

ret,frame = cap.read()
cv2.imshow('img', frame)
cv2.setMouseCallback('img', click_event)
cv2.waitKey(0)
cam_shit()

cap.release()
cv2.destroyAllWindows()
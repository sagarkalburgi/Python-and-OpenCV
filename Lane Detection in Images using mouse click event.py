# Lane Detection in images using mouse click event
"""
Right click -- To see your ROI

Left click -- To detect lanes

"""

import cv2
import numpy as np

def click_event(event, x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        img = cv2.imread('road.jpg')
        roi_ver = [(0, height), (x, y), (width, height)]

        gray_img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        canny_img = cv2.Canny(gray_img, 100, 200)
    
        cropped_img = roi(canny_img, np.array([roi_ver], np.int32))

        lines = cv2.HoughLinesP(cropped_img, rho=6, theta=np.pi/60,
                        threshold=160, lines=np.array([]),
                        minLineLength=40, maxLineGap=25)

        img_with_lines = draw_lines(img, lines)

        cv2.imshow('image', img_with_lines)
        return
    
    if event == cv2.EVENT_RBUTTONDOWN:
        img = cv2.imread('road.jpg')
        img = cv2.line(img, (0,height), (x,y), (0,255,0), 2)
        img = cv2.line(img, (width,height), (x,y), (0,255,0), 2)
        cv2.imshow('road', img)
        return

def roi(img, vertices):
    mask = np.zeros_like(img)
    match_mask_color = (255,) #* channel_count
    cv2.fillPoly(mask, vertices, match_mask_color)
    masked_img = cv2.bitwise_and(img, mask)
    cv2.imshow('masked', masked_img)
    return masked_img

def draw_lines(img, lines):
    img = np.copy(img)
    blank_img = np.zeros((img.shape[0], img.shape[1], 3), dtype=np.uint8)
    
    for line in lines:
        for x1, y1, x2, y2 in line:
            cv2.line(blank_img, (x1,y1), (x2,y2), (0,255,0), 2)
    
    img = cv2.addWeighted(img, 0.8, blank_img, 1, 0.0)
    return img
        
img = cv2.imread('road.jpg')

print(img.shape)
height = img.shape[0]
width = img.shape[1]

cv2.imshow('road', img)
cv2.setMouseCallback('road', click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()
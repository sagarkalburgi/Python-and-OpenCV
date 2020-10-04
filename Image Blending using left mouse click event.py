# Image Blending using left mouse click event

import cv2
import numpy as np

def click_event(event, x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        img12_pyr = []
        n = 0
        x = x//8
        for img1_lap, img2_lap in zip(lp_img1, lp_img2):
            n += 1 
            cols, rows, ch = img1_lap.shape
            laplacian = np.hstack((img1_lap[:,0:x//4], img2_lap[:, x//4:]))
            img12_pyr.append(laplacian)
            x += x
        
        img12_rec = img12_pyr[0]
        for i in range(1,6):
            img12_rec = cv2.pyrUp(img12_rec)
            img12_rec = cv2.add(img12_pyr[i], img12_rec)
            
        cv2.imshow('img_1', img_1)
        cv2.imshow('img_2', img_2)
        cv2.imshow('image reconstructed', img12_rec)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        return

#img_1 = cv2.imread('yellow.jfif')
#img_2 = cv2.imread('blue.jfif')
img_1 = cv2.imread('apple.jpg')
img_2 = cv2.imread('orange.jpg')

img_1 = cv2.resize(img_1, (512,512))
img_2 = cv2.resize(img_2, (512,512))

img1_level = img_1.copy()
gp_img1 = [img1_level]
for i in range(6):
    img1_level = cv2.pyrDown(img1_level)
    gp_img1.append(img1_level)
    
img2_level = img_2.copy()
gp_img2 = [img2_level]
for i in range(6):
    img2_level = cv2.pyrDown(img2_level)
    gp_img2.append(img2_level)
    
img1_level = gp_img1[5]
lp_img1 = [img1_level]
for i in range(5,0,-1):
    gaussian_extended = cv2.pyrUp(gp_img1[i])
    laplacian = cv2.subtract(gp_img1[i-1], gaussian_extended)
    lp_img1.append(laplacian)

img2_level = gp_img2[5]
lp_img2 = [img2_level]
for i in range(5,0,-1):
    gaussian_extended = cv2.pyrUp(gp_img2[i])
    laplacian = cv2.subtract(gp_img2[i-1], gaussian_extended)
    lp_img2.append(laplacian)
    
cv2.imshow('img_1', img_1)

cv2.setMouseCallback('img_1', click_event)

cv2.waitKey(0)
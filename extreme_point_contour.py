# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 00:10:15 2022

@author: Hp
"""

import cv2
import numpy as np

img = cv2.imread(r"C:\Users\Hp\Desktop\image\hand.jpg")
img = cv2.resize(img,(600,700))
img1 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


blur = cv2.medianBlur(img1, 7)
ret,thresh = cv2.threshold(blur,240,255,cv2.THRESH_BINARY_INV)

#findcontour(img,contour_retrival_mode,method)
cnts,hier = cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
#cv2.drawContours(img,cnts,-1,(50,50,150),2)

#here cnts is a list of contours. And each contour is an array with x
#hier variable called hierarchy and it contain image information.
print("number of contour==",cnts,"\ntotal contour===",len(cnts))
print("hierarchy==\n",hier)

#loop over the contours
for c in cnts:
    epsilon = 0.0001*cv2.arcLength(c, True)#here we use epsilon for storing ARC. and it is RANDOM variable named as elipson or epsilon
    data = cv2.approxPolyDP(c, epsilon, True)
    
    hull= cv2.convexHull(data)
    
    cv2.drawContours(img,[c],-1,(50,50,150),2)
    cv2.drawContours(img,[hull],-1,(0,255,0),2)

#Extreme point
#it means topmost,bottommost,rightmost and leftmost points of the object.

c_max = max(cnts, key=cv2.contourArea)

#determine the most extreme points along the contour

extLeft = tuple(c_max[c_max[:,:,0].argmin()][0])
extRight = tuple(c_max[c_max[:,:,0].argmax()][0])
extTop = tuple(c_max[c_max[:,:,1].argmin()][0])
extBot = tuple(c_max[c_max[:,:,1].argmax()][0])

#draw the outline of the object, then draw each of the  extreme points,where the left-most is red,
#right - most is green,top-most is blue,and bottom-most is teat

cv2.circle(img,extLeft,8,(255,0,255),-1)#pink
cv2.circle(img,extRight,8,(0,125,255),-1)#brown
cv2.circle(img,extTop,8,(255,10,0),-1)#blue
cv2.circle(img,extBot,8,(19,152,152),-1)#green


cv2.imshow("original===",img)
cv2.imshow("gray===",img1)
cv2.imshow("thresh==",thresh)


cv2.waitKey(0)
cv2.destroyAllWindows()


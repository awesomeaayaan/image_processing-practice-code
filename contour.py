# -*- coding: utf-8 -*-
"""
Created on Sun Feb  6 08:12:05 2022

@author: aayaan
"""
#Image Contours
#application of it are - it helps in shape detection analyzation and recognization
#Contours can be explained simply as a curve joining all the continuous points
#(along the boundary),having same color or intensity.

#The contours are a useful tool for shape analysis and object detection and 
#finding better accuracy, use binary images and also apply edge detection before finding coutours.
#findcontours function manipulate original image so copy it before proceeding.
#findcontour is like finding white object from black background
#so you must turn image in white and background is black.
#works always on graylevel image for efficient result
#we have to find and draw contours as per the requirement

import cv2
import numpy as np

img = cv2.imread(r"C:\Users\Hp\Desktop\image\logo.jpg")
img1 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)#first step convert to binary
ret,thresh = cv2.threshold(img1,70,255,0)#0 is simply binary method

#findcontour(img,contour_retrival_mode,method)-.cnts is a coordinate list generate by findcontour and hier is a hierarchy
cnts,hier = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

print(cnts,len(cnts))

#drawcontour(img,cnts,is of contour,color,thickness)-here if we draw contour we just pass -1
#draw contours
img = cv2.drawContours(img, cnts, -1, (25,100,15),4)

#output
cv2.imshow("original==",img)
cv2.imshow("gray==",img1)
cv2.imshow("thresh==",thresh)

cv2.waitKey(0)
cv2.destroyAllWindows()
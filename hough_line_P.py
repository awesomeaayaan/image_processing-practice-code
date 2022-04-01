# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 00:43:25 2022

@author: Hp
"""

import cv2
import numpy as np

#Second Type of Hough Transformation

img = cv2.imread(r"C:\Users\Hp\Desktop\image\chess.jpg")
img = cv2.resize(img,(400,400))
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray,50,150,apertureSize = 3)
cv2.imshow('edges', edges)
lines = cv2.HoughLinesP(edges,1,np.pi/180,100,minLineLength=8,
                        maxLineGap=100)
for line in lines:
    x1,y1,x2,y2 = line[0]
    cv2.line(img,(x1,y1),(x2,y2),(100,200,125),2)
cv2.imshow('image', img)
k = cv2.waitKey(0)
cv2.destroyAllWindows()

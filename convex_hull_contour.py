# -*- coding: utf-8 -*-
"""
Created on Sun Feb  6 09:54:03 2022

@author: Hp
"""
import cv2
import numpy as np

#-------------Contour Area , Approximation and Convex hull

#Find countour area , aprroximation and convex hull
img = cv2.imread(r"C:\Users\Hp\Desktop\image\shapes.png")
img = cv2.resize(img,(600,700))
img1 = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

ret,thresh = cv2.threshold(img1,220,255,cv2.THRESH_BINARY_INV)

#findcontour(img,contour_retrival_mode,method)
cnts,hier = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
#Here cnts is a list of contours. ANd each contour is an array with x, y cordinate   
#hier variable called hierarchy and it contain image information.
print("Number of contour==",cnts,"\ntotal contour==",len(cnts))
print("Hierarchy==\n",hier)



#draw contour
area1 = []
# loop over the contours
for c in cnts:
    # compute the center of the contour
    #an image moment is a certain particular weighted average (moment) of the image pixels
    M = cv2.moments(c)
    #print("M==",M)
    cX = int(M["m10"] / M["m00"])
    cY = int(M["m01"] / M["m00"])
    #find area of contour
    area = cv2.contourArea(c)
    area1.append(area)
    
    #contour Approx - it is use to approx shape with less number of vetices
    if area<10000:
        epsilon = 0.01*cv2.arcLength(c, True)
        data = cv2.approxPolyDP(c,epsilon,True)
        #Convexhull is used to provide proper contours convexity.
        
        hull = cv2.convexHull(data)
        
        x,y,w,h = cv2.boundingRect(hull)
        img = cv2.rectangle(img, (x,y), (x+w,y+h), (125,10,20),5)
        
    
 
    # draw the contour and center of the shape on the image
    cv2.drawContours(img, [c], -1, (50, 100, 50), 2)
    cv2.circle(img, (cX, cY), 7, (255, 255, 255), -1)
    cv2.putText(img, "center", (cX - 20, cY - 20),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
    
    
cv2.imshow("original===",img)
cv2.imshow("gray==",img1)
cv2.imshow("thresh==",thresh)
cv2.waitKey(0)


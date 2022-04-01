# -*- coding: utf-8 -*-
"""
Created on Sun Feb  6 09:09:30 2022

@author: aayaan
"""

#Contours and its functions
#MOMENT
#APPROXIMATION
#CONVEXHULL

import cv2
import numpy as np

img = cv2.imread(r"C:\Users\Hp\Desktop\image\shapes.png")
img = cv2.resize(img,(600,700))
img1 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(img1, 200, 255, cv2.THRESH_BINARY_INV)

#findcontours(img,contour_retrival_mode,method)
cnts,hier = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
#here cnts is a list of contours. And each contour is an array with x,
#hier variable called hierrarchy and it contain image information.

print("Number of contour==",cnts,"\ntotal contour==",len(cnts))
print("hierarchy==\n",hier)


#draw contour
#img = cv2.drawContours(img, cnts, -1, (10,20,100),4)

# loop over the contours
for c in cnts:
    # compute the center of the contour
    #an image moment is a certain particular weighted average (moment) of the image pixels
    M = cv2.moments(c)
    print("M==",M)
    cX = int(M["m10"] / M["m00"])
    cY = int(M["m01"] / M["m00"])
    # draw the contour and center of the shape on the image
    cv2.drawContours(img, [c], -1, (0, 255, 0), 2)
    cv2.circle(img, (cX, cY), 7, (255, 255, 255), -1)
    cv2.putText(img, "center", (cX - 20, cY - 20),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)



#output
cv2.imshow("original==",img)
cv2.imshow("gray==",img1)
cv2.imshow("tresh==",thresh)

cv2.waitKey(0)
cv2.destroyAllWindows()



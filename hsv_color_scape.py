#HSV-> hue Saturation Value
#with the help of hsv we easily separate the color information and color intensity
#if we want to detect something on the basis of color then HSV is very important

#detect color in image

import cv2
import numpy as np

frame = cv2.imread(r"C:\Users\Hp\Desktop\image\color_balls.jpg")

while True:
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    #u_v = np.array([130,235,225]) #for blue color ball
    #l_v = np.array([110,50,50])#for green color ball
    
    u_v = np.array([48,225,248])
    l_v = np.array([20,143,139])
    
    #create Mask
    mask = cv2.inRange(hsv,l_v,u_v)
    
    #filter mask with image
    res = cv2.bitwise_and(frame,frame,mask = mask)
    
    cv2.imshow("frame",frame)
    cv2.imshow("mask",mask)
    cv2.imshow("res",res)
    
    key = cv2.waitKey(1)
    if key == 27:
        break
    
cv2.destroyAllWindows()
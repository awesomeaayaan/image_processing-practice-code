#color detection with a track bar

import cv2
import numpy as np

frame = cv2.imread(r"C:\Users\Hp\Desktop\image\color_balls.jpg")
frame = cv2.resize(frame,(600,400))


def nothing(x):
    pass
cv2.namedWindow("color Adjustments")

cv2.createTrackbar("lower_H","color Adjustments",0,255,nothing)
cv2.createTrackbar("lower_S","color Adjustments",0,255,nothing)
cv2.createTrackbar("lower_V","color Adjustments",0,255,nothing)

cv2.createTrackbar("upper_H","color Adjustments",255,255,nothing)
cv2.createTrackbar("upper_S","color Adjustments",255,255,nothing)
cv2.createTrackbar("upper_V","color Adjustments",255,255,nothing)


while True:
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    l_h = cv2.getTrackbarPos("lower_H","color Adjustments")
    l_s = cv2.getTrackbarPos("lower_S","color Adjustments")
    l_v = cv2.getTrackbarPos("lower_V","color Adjustments")
    
    u_h = cv2.getTrackbarPos("upper_H","color Adjustments")
    u_s = cv2.getTrackbarPos("upper_S","color Adjustments")
    u_v = cv2.getTrackbarPos("upper_V","color Adjustments")


    lower_bound = np.array([l_h,l_s,l_v])
    upper_bound = np.array([u_h,u_s,u_v])
    
    
    mask = cv2.inRange(hsv,lower_bound,upper_bound)
    
    #filter mask with image
    res = cv2.bitwise_and(frame,frame,mask=mask)
    
    cv2.imshow("original frame",frame)
    cv2.imshow("mask",mask)
    cv2.imshow("res",res)
    
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break
    
cv2.destroyAllWindows()
        



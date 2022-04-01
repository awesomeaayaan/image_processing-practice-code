#image blending with trackbar

import cv2
import numpy as np
img1 = cv2.imread(r"C:\Users\Hp\Desktop\image\allu.jpg")
img1 = cv2.resize(img1,(500,700))#image size should be same of the two images
img2 = cv2.imread(r"C:\Users\Hp\Desktop\image\pic.jpg")
img2 = cv2.resize(img2,(500,700))#image size should be same of the two images
#cv2.imshow("allu",img1)
#cv2.imshow("my_pic",img2)

def blend(x):#it will simply pass the execution 
    pass

img = np.zeros((400,400,3),np.uint8)
cv2.namedWindow("win")#create the trackbar window
cv2.createTrackbar('alpha','win',1,100,blend)

#create a switch to ON/OFF
switch = '0:OFF\n 1 : ON'#create switch for invoke the trackbars
cv2.createTrackbar(switch,'win',0,1,blend)#create tack bar with switch

while True:
    s = cv2.getTrackbarPos(switch,"win")
    a = cv2.getTrackbarPos("alpha","win")
    n = float(a/100)
    print(n)
    
    if s == 0:#if s==0 then it will show the blank images
        dst = img[:]
    else:
        dst = cv2.addWeighted(img1,1-n,img2,n,0)#the weight of value should always equal to one i.e 1-n+n
        cv2.putText(dst,str(a),(20,50),cv2.FONT_ITALIC,2,(0,125,255),5)
        
    cv2.imshow('dst',dst)
    k = cv2.waitKey(1) & 0xFF
    if k == ord("q"):
        break

cv2.waitKey(0)
cv2.destroyAllWindows()

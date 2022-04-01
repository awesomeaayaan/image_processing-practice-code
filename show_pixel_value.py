#create a function which help to find cordinate of any pixel and its color

import cv2
import numpy as np

def mouse_event(event,x,y,flg,param):
    print("event ==",event)
    print("x ==",x)
    print("y==",y)
    print("flg== ",flg)
    print("param==",param)
    
    
    
    font = cv2.FONT_HERSHEY_PLAIN
    if event == cv2.EVENT_LBUTTONDOWN:#if left button single click then it will show x,y value
        print(x,',',y)
        cord = '.'+str(x)+','+str(y)
        cv2.putText(img,cord,(x,y),font,1,(155,125,100),2)
        #cv2.imshow("image",img)
        
        
    if event == cv2.EVENT_RBUTTONDOWN:#in single click it will provide a data
        b = img[y,x,0]#for blue channel is 0,it will give bluecolor value of pixel
        g =img[y,x,1]#for green channel is 1,it will give greencolor value of pixel
        r = img[y,x,2]#for red channel is 2,it will give redcolor value of pixel
        
        color_bgr = "."+str(b)+','+str(g)+','+str(r)
        cv2.putText(img,color_bgr,(x,y),font,1,(152,255,130),2)
        #cv2.imshow("image",img)
        
cv2.namedWindow(winname = "res")

img = np.ones((512,512,3),np.uint8)#it is used to draw a black image
cv2.setMouseCallback("res", mouse_event)

while True:
    cv2.imshow("res",img)
    if cv2.waitKey(3) & 0xFF == ord("q"):
        break

cv2.destroyAllWindows()

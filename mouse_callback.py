#mouse call back function
import cv2
import numpy as np

def draw(event,x,y,flg,param):#x,y shows the cordinates of mouse where it is moving and flags show 0 if we click left and 1 if we click right
    print("event ==",event)
    print("x ==",x)
    print("y==",y)
    print("flg== ",flg)
    print("param==",param)

    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img,(x,y),100,(125,0,255),5)
    if event == cv2.EVENT_RBUTTONDBLCLK:
        cv2.rectangle(img,(x,y),(x+100,y+75),(125,125,255),2)
        
        
cv2.namedWindow(winname = "res")

img = np.zeros((512,512,3),np.uint8)#it is used to draw a black image
cv2.setMouseCallback("res", draw)

while True:
    cv2.imshow("res",img)
    if cv2.waitKey(3) & 0xFF == ord("q"):
        break

cv2.destroyAllWindows()

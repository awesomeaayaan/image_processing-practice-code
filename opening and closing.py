 #two more basic morphological transformation are
#1-opening and 2-closing

import cv2
import numpy as np


#opening
#it is the combination of erosion and dilution i.e another name of erosion followed by dilation
#means first erosion take place and then dilation take place

img = cv2.imread(r"C:\Users\Hp\Desktop\image\col_balls.jpg",0)
_, mask = cv2.threshold(img, 230, 255, cv2.THRESH_BINARY_INV)
kernel = np.ones((3,3),np.uint8)#3*3 kernel with full of ones.
o = cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernel)#optional parameters iterations = 2


cv2.imshow("img",img)
cv2.imshow("ker=",kernel)
cv2.imshow("mask ==",mask)
cv2.imshow("Opening==",o)

#closing
#it is opposite of opening
#closing is just another name of dilatio followed by erosion.
#means first dilation take place and then erosion take place
img = cv2.imread(r"C:\Users\Hp\Desktop\image\col_balls.jpg",0)
_, mask = cv2.threshold(img, 230, 255, cv2.THRESH_BINARY_INV)
kernel = np.ones((3,3),np.uint8)#3*3 kernel with full of ones.
c = cv2.morphologyEx(mask,cv2.MORPH_CLOSE,kernel)#optional parameters iterations = 2
cv2.imshow("Closing==",c)


cv2.waitKey(0)
cv2.destroyAllWindows()
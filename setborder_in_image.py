#set the border in the image

import cv2
import numpy as np
img = cv2.imread(r"C:\Users\Hp\Desktop\image\lion1.jpg")
img = cv2.resize(img,(1000,600))

#create a border to the images
brdr = cv2.copyMakeBorder(img, 15, 15, 15, 15,cv2.BORDER_CONSTANT,value=[125,100,120])
cv2.imshow("lion",brdr)
cv2.waitKey(0)
cv2.destroyAllWindows()


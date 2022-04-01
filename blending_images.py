
#Image Blending with open cv

import cv2
import numpy as np

#in image blending we use two important function cv2.add(),cv2.addWeight()
#simply blending means additon of two images
#if you want to blend two images then both have same size

img1 = cv2.imread(r"C:\Users\Hp\Desktop\image\roi_opr.jpg")
img1 = cv2.resize(img1,(500,600))
img2 = cv2.imread(r"C:\Users\Hp\Desktop\image\bro_thor.jpg")
img2 = cv2.resize(img2,(500,600))

cv2.imshow("thor==",img1)
cv2.imshow("bro_thor==",img2)
#now perform blending function 
#result = img1 + img2 #numpy addition in this we get module between the value(don't use this)
#result = cv2.add(img1,img2)#always use cv2.add
#cv2.imshow("result",result)

#extended function of add i.e addWeight
#function cv2.addWeighted(img1,wt1,img2,wt2,gama_val)
result2 = cv2.addWeighted(img1,0.5,img2,0.5,0)#weight value always equal to 1 i.e 0.7+0.3 = 1
cv2.imshow("result",result2)

cv2.waitKey(0)
cv2.destroyAllWindows()


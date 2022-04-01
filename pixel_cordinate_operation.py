#image operation with pixels and cordinates

import cv2
import numpy as np


#read am an image
img = cv2.imread(r"C:\Users\Hp\Desktop\owl-images.jpg")

img1 = cv2.resize(img,(600,600))
'''
print("shape==",img1.shape)#it will returns the no. of rows and columns and channel
print("no.of pixels ==",img1.size)#it will returns a total number of pixel that were access
print("datatypes==",img1.dtype)#returns the datatype 
print("Imagetypes==",type(img1))
'''
#now we are try to split an images
#split-> return 3 channel of ur image which is blue,green,red
print(cv2.split(img1))

b,g,r = cv2.split(img1)#it will split the 3 images of red blue and green

cv2.imshow("blue",b)
cv2.imshow("green",g)
cv2.imshow("red",r)

'''
#Now if you want to mix the the channels then use merge

mr1 = cv2.merge((r,g,b))
cv2.imshow("rgb",mr1)
mr2 = cv2.merge((g,b,r))
cv2.imshow("gbr",mr2)


cv2.imshow("original",img1)
cv2.waitKey(0)
cv2.destroyAllWindows()

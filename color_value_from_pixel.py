import cv2
import numpy as np

img = cv2.imread(r"C:\Users\Hp\Desktop\owl-images.jpg")
img1 = cv2.resize(img,(600,600))

cv2.imshow("lion",img1)

#access a pixel value by its row column coordinates.
px = img1[520,580] #store cordinate in variable
print("the pixel of that coordiante is ==",px)

#try to find selected value from the coordinates
#as we know for rgb we have 3 channel - 0,1,2
#now accessing only blue pixel
blue = img[520,580,0]#for blue pass 0
print("the pixel having blue color ==",blue)

grn = img[520,580,1]#for green pass1
print("the pixel having green colorr ==",grn)

red = img[520,580,2]#for red pass 2
print("the pixel having red color ==",red)

cv2.waitKey(0)
cv2.destroyAllWindows()


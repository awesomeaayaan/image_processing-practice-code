#Adaptive thresholding
#we use it because simple thresholding not able to handle different types ofo low luminious pixels
#this algorithm calculate the threshold for small regions of the images. there is high chance of data 
#loss in case of simple thresholdig so adaptive thresholding is important
#hence we get multiple threshold for diff. regiions in same image.

#Adaptive Method - it decides how thresholding value is calculated
#cv2.ADAPTIVE_THRESH_MEAN_c :it will works on neighbour mean values
#cv2.ADAPTIVE-THRESH_GAUSSIAN_C :it will works on the average value of the neighbour

#threshold (img, pixel_thresh,_max_thresh_pixel,methd,style,no.of_pixel,contact_mean)
import cv2
import numpy as np

img = cv2.imread(r"C:\Users\Hp\Desktop\image\page.jpg",0)
img = cv2.resize(img,(400,400))

_, th1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY) #simple thresholding

th2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)
#no data lost as seen in simple thresholding so we implement adaptive method

th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)

cv2.imshow("image",img)
cv2.imshow("THRESH_BINARY",th1)
cv2.imshow("adaptive 1==",th2)
cv2.imshow("Gaussian 2==",th2)


cv2.waitKey(0)
cv2.destroyAllWindows()

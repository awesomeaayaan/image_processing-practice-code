#extracting the the object from one image and place it into the another images 
#random figure ROI or background subtraction.

import cv2
import numpy as np

#load two images
img1 = cv2.imread(r"C:\Users\Hp\Desktop\image\hero1.jpg")
img2 = cv2.imread(r"C:\Users\Hp\Desktop\image\strom_breaker.jfif")

img1 = cv2.resize(img1,(1024,650))#the holding image should have its size always larger
img2 = cv2.resize(img2,(600,650))#this image size is less because we took this image to img1 so took image with less or equal to holding image

#i want of fix image 2 data into img1
r,c,ch = img2.shape #r-row,c-column,ch-channel -> get the image size from image 2 now in below it is pass to img1 
print(r,c,ch)

#create roi == where you have to place a second image in first image
roi = img1[0:r,0:c] #pass the size of image2 to image 1

#now creating mask for img2
img_gry = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

#creating mask using thresholding
_, mask = cv2.threshold(img_gry,50,255,cv2.THRESH_BINARY) #the pixel value less than 50 covert to black and above 5o convet to white so image will be seen clearly


#remove background
mask_inv = cv2.bitwise_not(mask)

#put mask into roi
img1_bg = cv2.bitwise_and(roi,roi,mask = mask_inv)



#take only region of figure from original image.
img2_fg = cv2.bitwise_and(img2,img2,mask=mask)


#put img in roi and modify the main image
res = cv2.add(img1_bg,img2_fg)

final = img1 
final[0:r,0:c]= res #final output


#cv2.imshow("thor",img1)
#cv2.imshow("strom breaker",img2)
#cv2.imshow("roi==",roi)
cv2.imshow("step -1 gry ==",img_gry)
cv2.imshow("step -2 mask==",mask)
cv2.imshow("step -3 mask_inv",mask_inv)
cv2.imshow("step -4 mask_bg",img1_bg)
cv2.imshow("step -5 mask fg",img2_fg)#get color in image
cv2.imshow("step -6 res",res)
cv2.imshow("step-7==",final)





cv2.waitKey()
cv2.destroyAllWindows()


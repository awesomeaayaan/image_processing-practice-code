#morphological transformation
#morphological transformation are some simple operation based on the image shape
#it is normally performed on binary images.
#it need two inputs, 1- original image, 2-structuring element(kernel).
#two basic morphological transformation are 1- eriosio and 2-dilation



import cv2
import numpy as np

#Erosion
#it erodes away the boundaries of foreground objects
#kernal slides through all the image and all the pixel 
#from the original image conside 1 only if kernel's pixel is 1

img = cv2.imread(r"C:\Users\Hp\Desktop\image\col_balls.jpg",0)
_, mask = cv2.threshold(img, 230, 255, cv2.THRESH_BINARY_INV)
kernel = np.ones((5,5),np.uint8)#5*5 kernel with full of ones.
e = cv2.erode(mask,kernel)



#Dilation
#it is just opposite of erosion. 
#Here, a pixel element is '1' if atleast one pixel under the kernel is '1' 
# so it include the white region in the image or size of forground object in.
#normally, in cases like noise removal, erosion is followed by dilation.
#Because, erosion removes white noises, but it also shrinks our object.

kernel = np.ones((4,4),np.uint8)
d = cv2.dilate(mask,kernel)#iterations = 2(optional parameters) iterations
cv2.imshow("dilate==",d)

#if you want to plot it 
from matplotlib import pyplot as plt
titles = ["img","mask","erosion","dilation"]
images = [img,mask,e,d]
for i in range(4):
    plt.subplot(2,2,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
    
    
plt.show()





cv2.imshow("img",img)
cv2.imshow("ker=",kernel)
cv2.imshow("mask ==",mask)
cv2.imshow("erosion==",e)

cv2.waitKey(0)
cv2.destroyAllWindows()
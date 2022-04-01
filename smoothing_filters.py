#image smoothing or bluring is most common used operation in Image Processing.
#It is use to remove noise from the images
#There is so many filter which is use for smoothing the image.
#There are Low pass Filter (LPS) which is use to remove noise from the images.
#There are High pass Filter which use to detect and finding edges in an images.

#we discuss about various filters ---
# like, homogeneous,blur(averaging),gaussian,median,bilateral


import cv2
import numpy as np

img = cv2.imread(r"C:\Users\Hp\Desktop\image\noisy2.jpg")
img = cv2.resize(img,(400,400))
cv2.imshow("original==",img)

kernel = np.ones((5,5),np.float32)/25

#Filter Number - 1(2-d convolution filter/homogeneous filter)
#this filter work like, each output pixel is the mean of its kernal neighbour
#it is a homogeneous filter in this all pixel contribute with equal weight.
#kernal is a small shape or matrix which we apply on image.
#in this filter kernal is [(1/kernel(h,w))*kernel]

h_filter = cv2.filter2D(img, -1, kernel) #-1 is the desired depth
cv2.imshow("homogeneous==",h_filter)

#averaging method/blurr method filter
#take the average of all pixels under kernel area and replace the central element with this average..

blur = cv2.blur(img,(8,8))#here we have image and kernel as parameter
cv2.imshow("blur==",blur)


#Gaussian Filter
#here it is using differnent weight kernel , in row as well as column
#means side values are small then centre. It manage distance b/w value of pixel

gau = cv2.GaussianBlur(img, (5,5), 0) #here 0 is sigma x value/color value
cv2.imshow("gau blurr=",gau)

#Median filter --computed the median of all the pixels under the kernel windodw
#and the central pixel is replaced with this median value.
#this is highly effective in removing salt- and -pepper noise.
#here kernel size must be odd except one

med = cv2.medianBlur(img,5)#kernel value should be always odd
cv2.imshow("median filter",med)

#bilateral filter 
#it is highly effectively at noise removal while preserving edges
#it is slow as compared with other filters
#argument (img, neighbour_pixel_diameter,sigma_color,sigma_space)

bi_f = cv2.bilateralFilter(img, 5, 75, 75)#neighbourpixel=9,sigmacolor=75,sigmaspace=75 in documentation but we set the value 50 to 100 also
cv2.imshow("bi_f",bi_f)

#now plot all the image on the graph
titles = ["original","homo","blur","gauss","med","bi_f"]
images = [img,h_filter,blur,gau,med,bi_f]

#if you want to plot it 
from matplotlib import pyplot as plt
for i in range(6):
    plt.subplot(2,3,i+1),
    plt.imshow(images[i],"gray")
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
    
plt.show()




cv2.waitKey(0)
cv2.destroyAllWindows()

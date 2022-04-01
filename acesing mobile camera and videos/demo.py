import cv2 #opencv use as cv2 in python
'''
#load image in color mode
img1 = cv2.imread("C:\\Users\\Hp\\Desktop\\1st.jpg.JPG",1)
img1 = cv2.resize(img1,(1280,700)) #width and height
print(img1)
cv2.imshow("original",img1)

#cv2.imread_grayscale:load image in grayscale mode
img2 = cv2.imread("C:\\Users\\Hp\\Desktop\\1st.jpg.JPG",0)#convert color to gray scale image
img2 = cv2.resize(img2,(1280,700)) #width and height
print("gray scale image",img2)
cv2.imshow("grayscale image",img2)

#load image by unchanging it
img3 = cv2.imread("C:\\Users\\Hp\\Desktop\\1st.jpg.JPG")
img3 = cv2.resize(img3,(1280,700)) #width and height
print(img3)
cv2.imshow("unchange image",img3)




cv2.waitKey(3000)
cv2.destroyAllWindows()
'''
#image conversion project- colored image to grayscale image
path= input("enter the path and name of the image: ")
print("your enter image is: ",path)

img1 = cv2.imread(path,0)
img1 = cv2.resize(img1,(1280,700)) #width and height
print(img1)
cv2.imshow("converted image is :",img1)

cv2.waitKey()
cv2.destroyAllWindows()



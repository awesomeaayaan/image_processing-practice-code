#drawing function in opencv

import numpy as np
import cv2

img = cv2.imread(r"C:\Users\Hp\Desktop\image\aayaan1.jpg")
img = cv2.resize(img,(600,700))
'''
to drawa a line we should have to pass a 5 parameter(img,starting,ending,color,thickness)
here we draw a line in a image
'''
img = cv2.line(img,(0,0),(200,200),(154,92,424),8)
#drawing arrowed line that also accept 5 parameters (img,starting ,ending,color,thickness)
img = cv2.arrowedLine(img, (0,125), (255,255),(255,0,125),5)

#drawing rectangel accept parameter(img,star-cod,end-cod,color,thickness)
img = cv2.rectangle(img, (100,200), (400,500), (150,72,120),10)#if we fill thickness value with -1 it will fill the same color to whole rectangle

#circle - accept(img,star_cod,radius,color,thickness)
img = cv2.circle(img,(447,125),65,(214,255,0),-1)

#if we want to put some text in the image
font = cv2.FONT_ITALIC
#puttext-accept(img,text,star_co,font,fontsize,color,thickness,linetype)
img= cv2.putText(img,"marriage_photo",(20,500),font,4,(0,125,255),5,cv2.LINE_AA)

#ellipse-accepting(img,start_co,(length,height),color,thickness)
img = cv2.ellipse(img,(400,600),(100,50),0,0,360,125,5)#here 0,0 is a rotation point 360 is the angle and 155 is the color code,5 is thickness


cv2.imshow("res",img)
cv2.waitKey()
cv2.destroyAllWindows()
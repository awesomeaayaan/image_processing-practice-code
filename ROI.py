#region of interest(ROI)
#ROI-> Region of INTEREST
import numpy as np
import cv2

img = cv2.imread(r"C:\Users\Hp\Desktop\image\pic.jpg")
img = cv2.resize(img,(800,800))#width,height

#ROI (regionof interest)
#(355,150) (x1,y1)
#(490,325)(x2,y2)
#[(y1:y2),(x1:x2)]
#diff on y=175,x= 135
roi = img[145:320,350:485]

#now passing data into the images
img[145:320,491:626] = roi
img[145:320,627:762]=roi
img[145:320,215:350] = roi
img[145:320,80:215] = roi

#changing the y axis
img[320:495,350:485] = roi

img1 = cv2.imread(r"C:\Users\Hp\Desktop\image\allu.jpg")
img1 = cv2.resize(img1,(900,600))
img1[1:176,425:560] = roi

cv2.imshow("allu",img1)

cv2.waitKey(0)
cv2.destroyAllWindows()
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 11 15:42:14 2022

@author: Hp
"""

import cv2
import face_recognition

img = cv2.imread(r"C:\Users\Hp\Desktop\image\aayaan12.jpg")
rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_encoding = face_recognition.face_encoding(rgb_img)[0]



cv2.imshow("img",img)

cv2.waitKey(0)
cv2.destroyAllWindows()
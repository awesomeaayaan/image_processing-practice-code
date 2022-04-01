#bitwise operation include AND, OR, NOT and XOR
#it is most important and use for various prupose like masking and find roi which is in complex

import cv2
import numpy as np

img1 = np.zeros((250,500,3),np.uint8)
img1 = cv2.rectangle(img1,(150,100),(200,250),(255,255,255),-1)

img2 = np.zeros((250,500,3),np.uint8)
img2 = cv2.rectangle(img2,(10,10),(170,190),(255,255,255),-1)

cv2.imshow("img1",img1)
cv2.imshow("img2",img2)
'''
bitAnd = cv2.bitwise_and(img2,img1)
cv2.imshow('bitAnd',bitAnd)
'''
#bitOr = cv2.bitwise_or(img2,img1)
#cv2.imshow('bitor',bitOr)

bitNot1 = cv2.bitwise_not(img1)
cv2.imshow('bitNot1',bitNot1)
bitNot2 = cv2.bitwise_not(img2)
cv2.imshow('bitNot2',bitNot2)

#bitXor = cv2.bitwise_xor(img2,img1)
#cv2.imshow('bitXor',bitXor)




cv2.waitKey(0)
cv2.destroyAllWindows()
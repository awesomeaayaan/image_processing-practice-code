#thresholding 
import cv2
import numpy as np

imag = cv2.imread(r"C:\Users\Hp\Desktop\image\black_white.png",0)
imag = cv2.resize(imag,(300,300))
imag = cv2.imshow("original",imag)

_, th1 = cv2.threshold(imag, 50, 255, cv2.THRESH_BINARY)

cv2.imshow("THRESH_BNARY",th1)

#cv2.imshow("1 - THRESH_BINARY",th1)

cv2.waitKey(0)
cv2.destroyAllWindows()

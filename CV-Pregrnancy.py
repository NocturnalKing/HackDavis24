import cv2 as cv
import numpy as np

img = cv.imread('Bob/1_2HC.png')

#cv.imshow("Pregnancy" , img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)
#works the best so far

# #Edge cascade
canny = cv.Canny(blur, 125, 175)

ret, thresh = cv.threshold(gray, 125, 255, 0)
contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE) 
cv.drawContours(img, contours, -1, (0,255,0), 3) 
area = cv.contourArea(contours[0]) 
scale_factor = 0.1
size = area * scale_factor ** 2

print("size:", size)
cv.imshow("Pregnacy", canny)


#laplacion, edge detection
# lap = cv.Laplacian(gray,cv.CV_64F)
# lap = np.uint8(np.absolute(lap))
# cv.imshow('Laplacian', lap)

#sobel
# sobelx = cv.Sobel(gray, cv.CV_64F, 1, 0)
# sobely = cv.Sobel(gray, cv.CV_64F, 0, 1)

# cv.imshow('Sobel X', sobelx)
# cv.imshow('Sobel Y', sobely)

cv.waitKey(0)

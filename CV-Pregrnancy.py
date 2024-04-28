import cv2 
import numpy as np

image = cv2.imread('Bob/1_2HC.png')

blurred_img = cv2.GaussianBlur(image, (21, 21), 0)
mask = np.zeros(image.shape, np.uint8)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY)[0]
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(mask, contours, -1, (255,255,255),5)
# output = np.where(mask==np.array([255, 255, 255]), blurred_img, image)

# kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
# im = cv.filter2D(img, -1, kernel)
# cv.imshow("Imageeee", im)

#image sharpening
gaussian_blur = cv.GaussianBlur(img, (7,7), 2)
sharpened = cv.addWeighted(img, 3.5, gaussian_blur, -2.5, 0)

cv2.imshow('Sharpened', sharpened)

# #cv.imshow("Pregnancy" , img)

# # gray = cv.cvtColor(sharpened, cv.COLOR_BGR2GRAY)
# # cv.imshow('Gray', gray)
# blur = cv.GaussianBlur(im, (7,7), cv.BORDER_DEFAULT)


# cv.imshow('Blur', blur)
# #works the best so far

# # #Edge cascade
# canny = cv.Canny(blur, 125, 175)

# ret, thresh = cv.threshold(sharpened, 40, 255, 0)
# contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE) 
# # cv.drawContours(canny, contours, -1, (0,255,0), 3) 
# # area = cv.contourArea(contours[0]) 
# # scale_factor = 0.1 #bad value to use, originally was 0.1, i dont really know.
# # size = area * scale_factor ** 2

# count = contours[0]
# print("count", count)
# def find_solidity(count): 
#     contourArea = cv.contourArea(count) 
#     convexHull = cv.convexHull(count) 
#     contour_hull_area = cv.contourArea(convexHull) 
#     solidity = float(contourArea)/contour_hull_area 
#     return solidity 

# Solidity = find_solidity(count) 
# Solidity = round(Solidity, 2) 
# def find_equi_diameter(count): 
#     area = cv.contourArea(count) 
#     equi_diameter = np.sqrt(4*area/np.pi) 
#     return equi_diameter 

# print("Diameter" , find_equi_diameter(count))
# # print(area)
# # print("size:", size)
# cv.imshow("Pregnacy", canny)


#laplacion, edge detection
# lap = cv.Laplacian(gray,cv.CV_64F)
# lap = np.uint8(np.absolute(lap))
# cv.imshow('Laplacian', lap)

#sobel
# sobelx = cv.Sobel(gray, cv.CV_64F, 1, 0)
# sobely = cv.Sobel(gray, cv.CV_64F, 0, 1)

# cv.imshow('Sobel X', sobelx)
# cv.imshow('Sobel Y', sobely)


#cv.imshow("Pregnancy" , img)

# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray', gray)
# blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
# cv.imshow('Blur', blur)
# #works the best so far

# # #Edge cascade
# canny = cv.Canny(blur, 125, 175)

# ret, thresh = cv.threshold(gray, 125, 255, 0)
# contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE) 
# cv.drawContours(img, contours, -1, (0,255,0), 3) 
# area = cv.contourArea(contours[0]) 
# scale_factor = 0.1
# size = area * scale_factor ** 2

# print("size:", size)
# cv.imshow("Pregnacy", canny)

"""" commented:
laplacion, edge detection
 lap = cv.Laplacian(gray,cv.CV_64F)
 lap = np.uint8(np.absolute(lap))
 cv.imshow('Laplacian', lap)

sobel
 sobelx = cv.Sobel(gray, cv.CV_64F, 1, 0)
 sobely = cv.Sobel(gray, cv.CV_64F, 0, 1)

 cv.imshow('Sobel X', sobelx)
 cv.imshow('Sobel Y', sobely)
"""

cv2.waitKey(0)

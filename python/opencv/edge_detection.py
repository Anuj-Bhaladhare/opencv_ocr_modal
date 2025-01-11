import cv2 as cv
import numpy as np


image = cv.imread(r"C:\Users\kkamb\OneDrive\Desktop\code_learn\python\opencv\photos\cat_large.jpg");
cv.imshow('Image',image)

image2 = cv.imread(r"C:\Users\kkamb\OneDrive\Desktop\code_learn\python\opencv\photos\cctv.jpg");
cv.imshow('Image',image2)

gray2=cv.cvtColor(image2,cv.COLOR_BGR2GRAY)
gray=cv.cvtColor(image,cv.COLOR_BGR2GRAY)
# cv.imshow('Image Gray',gray)
#laplacian gray is input image, desired depth of the image:- cv.CV_64F,kernal size must be in
# odd numbers 1,3,5,9,7 by default 1
laplacian=cv.Laplacian(gray2,cv.CV_64F,ksize=1)
print(laplacian)
cv.imshow('Laplacian',laplacian)

#Sobel gray is input image ,cv.cv_64f is a output depth of the image, 1 x direction,0- y direction
sobelx=cv.Sobel(gray2,cv.CV_64F,1,0)
sobely=cv.Sobel(gray2,cv.CV_64F,0,1)
#sobelx and sobely is an input
combine_sobel=cv.bitwise_or(sobelx,sobely)

# cv.imshow('Soblex',sobelx)
# cv.imshow('Sobely',sobely)
cv.imshow('Combined Sobel',combine_sobel)

#canny detection
canny=cv.Canny(gray2,50,50)
cv.imshow('Canny image',canny)

#
cv.waitKey(0)
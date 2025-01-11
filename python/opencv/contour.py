import cv2 as cv
import numpy as np

image=cv.imread(r"C:\Users\kkamb\OneDrive\Desktop\code_learn\python\opencv\photos\cat_large.jpg");

#converting an image into greyscale
grey=cv.cvtColor(image,cv.COLOR_BGR2GRAY)
cv.imshow('Grey',grey)

#converting an image into blur
blur=cv.GaussianBlur(grey,(5,5),1)
print(blur)
cv.imshow('Blur',blur);

#converting an image into edge detection
edge=cv.Canny(blur,10,10);
print(edge)
cv.imshow('Edge',edge);

#find contours
contours,hierarchy=cv.findContours(edge,cv.RETR_TREE,cv.CHAIN_APPROX_NONE)
# print(contours)
# cv.imshow("Coutours", contours);

cv.waitKey(0);
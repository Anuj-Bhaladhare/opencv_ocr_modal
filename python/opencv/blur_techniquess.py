import cv2 as cv

image=cv.imread(r"C:\Users\kkamb\OneDrive\Desktop\code_learn\python\opencv\photos\cat_large.jpg");

#averaging

avgimage=cv.blur(image,(5,5));

cv.imshow("Average Image", avgimage);

#Gaussian Blur
gaussianBlur=cv.GaussianBlur(image,(5,5),1);
cv.imshow('Gaussian Blur',gaussianBlur);

#Median Blur
medainBlur=cv.medianBlur(image,1);
cv.imshow('Median Blur',medainBlur);


#Bilateal blur
bilateral=cv.bilateralFilter(image,15,75,75)
cv.imshow('Bilateral blur', bilateral)


cv.waitKey(0);
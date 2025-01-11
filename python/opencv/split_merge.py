import cv2 as cv
import numpy as np

image=cv.imread(r"C:\Users\kkamb\OneDrive\Desktop\code_learn\python\opencv\photos\cat_large.jpg");

blank=np.zeros(image.shape[:2],'uint8');
cv.imshow('Blank',blank);



#split the image
b,g,r=cv.split(image);

# cv.imshow('Blue', b);
# cv.imshow('Green',g);
# cv.imshow('Red',r);

print(image.shape);
print(b.shape);
print(g.shape);
print(r.shape);

#merged the image b g r
merged=cv.merge([b,g,r]);
cv.imshow("merged",merged);




blue=cv.merge([b,blank,blank]);
green=cv.merge([blank,g,blank]);
red=cv.merge([blank,blank,r]);
cv.imshow('Blue',blue);
cv.imshow('Green',green);
cv.imshow('Red',red);



cv.imshow('image', image);
cv.waitKey(0);
import cv2 as cv
import numpy as np

image=cv.imread(r"C:\Users\kkamb\OneDrive\Desktop\code_learn\python\opencv\photos\cat_large.jpg");

image2=cv.resize(image,(400,500), interpolation=2);

#Translation
# -x:- left
# -y:- up
# x:- right
# y:-down
def translation(image, x,y):
    T=np.float32([[1,0,x],[0,1,y]]);
    dimension=(image.shape[1], image.shape[0]);
    return cv.warpAffine(image,T, dimension);

translate=translation(image,-100,100);
cv.imshow("Translate", translate);


#Rotation

rotate=cv.rotate(image,cv.ROTATE_180);
cv.imshow('rotate', rotate);

#Resize
resize=cv.resize(image,(400,400),interpolation=cv.INTER_CUBIC);
cv.imshow('Resized image', resize);

#flipping the image
flip=cv.flip(resize,-1);
cv.imshow('Flip', flip);

#cropping the image
crop=resize[70:180,200:300];
cv.imshow('Crop',crop);





# cv.imshow('Cat', image);
cv.imshow('Resized image',image2);


cv.waitKey(0);
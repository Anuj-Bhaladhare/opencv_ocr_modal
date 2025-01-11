import cv2 as cv
import matplotlib.pyplot as plt

image=cv.imread(r"C:\Users\kkamb\OneDrive\Desktop\code_learn\python\opencv\photos\cat_large.jpg");

cv.imshow('Image',image);

# plt.imshow(image);
# plt.show();
# convert image to greyscale
grey=cv.cvtColor(image,cv.COLOR_RGB2GRAY);
cv.imshow('Grey',grey);

#rgb to hue saturation value

hsv=cv.cvtColor(image,cv.COLOR_BGR2HSV);
cv.imshow('HSV', hsv);

#rgb to lab- Luminance a , b
lsv=cv.cvtColor(image,cv.COLOR_BGR2LAB);
cv.imshow('lsv',lsv);

#bgr to rgb
bgr=cv.cvtColor(image,cv.COLOR_BGR2RGB);
# cv.imshow('bgr',bgr);
plt.imshow(bgr);
plt.show();

# hsv to bgr
hsv=cv.cvtColor(image,cv.COLOR_HSV2BGR);
plt.imshow("hsv",hsv);
plt.show();

cv.waitKey(0);
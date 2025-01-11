import cv2 as cv
import numpy as np

image = cv.imread(r"C:\Users\kkamb\OneDrive\Desktop\code_learn\python\opencv\photos\cat_large.jpg");
blank=np.zeros(( 500,500,3),dtype='uint8');
cv.imshow('Blank', blank);


# paint a frame to a certain color
# blank[200:300,300:400]=0,0,0
# cv.imshow('Green',blank);

# # draw a rectangle
# cv.rectangle(image ,(10,10),(image.shape[1]//2,blank.shape[0]//2),(0,55,143),thickness=3 ,lineType=1);
# cv.imshow('Rectangle', image );


# #draw a circle

# cv.circle(blank, (blank.shape[1]//2,blank.shape[0]//2), 40,(0,255,2), thickness= 3);
# cv.imshow('Circle', blank);

# cv.circle(blank, (255,255),40,(255,2,55),thickness= -1);
# cv.imshow('Circle', blank);

# # draw a line
# cv.line(blank,(0,0),(255,255),(0,255,0),thickness=2);
# cv.imshow('line', blank);


# cv.imshow('Cat', image);

# draw a text
cv.putText(blank,'Hi there is opencv', (2,255), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,55,56), thickness=2);
cv.imshow('Text', blank);
cv.putText()
cv.waitKey(0);
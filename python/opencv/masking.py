import cv2 as cv
import numpy as np

cat=cv.imread(r"C:\Users\kkamb\OneDrive\Desktop\code_learn\python\opencv\photos\cat_large.jpg")
blank=np.zeros(cat.shape[:2],dtype='uint8')
cv.imshow('Blank',blank);

mask=cv.circle(blank.copy(),(cat.shape[1]//2, cat.shape[0]//2),50,(255,0,255),-1)
cv.imshow('Mask',mask)

rectangle=cv.rectangle(blank.copy(),(30,30),(250,250),(0,255,255),-1)
cv.imshow('Rectangle',rectangle)

#mask using the rectangle
# rectangle=cv.rectangle(blank,(cat.shape[1]//2,cat.shape[0]//2),(cat.shape[1]//2,cat.shape[0]//2),50,255,-1)
# cv.imshow('Rectangle Mask',rectangle)



# #bitwise_and operation perform
bitwise=cv.bitwise_and(cat,cat,mask=mask);
cv.imshow('Bitwise and',bitwise)


cv.imshow('Cat Image',cat)
cv.waitKey(0)
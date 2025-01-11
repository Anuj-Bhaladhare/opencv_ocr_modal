import cv2 as cv
import matplotlib.pyplot as mp
import numpy as np

img=cv.imread(r"C:\Users\kkamb\OneDrive\Desktop\code_learn\python\opencv\photos\img.jpg")

blank=np.zeros(img.shape[:2],dtype='uint8');

cv.imshow('Image',img)
#greyscale 
grey=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Grey Scale',grey)

mask=cv.circle(blank.copy(),(img.shape[1]//2,img.shape[0]//2),100,255,-1)
# cv.imshow('Circle',circle)

masked=cv.bitwise_and(img,img,mask=mask)
cv.imshow('Mask',masked)


# #histogram
gray_histo=cv.calcHist([grey],[0],None,[256],[0,256])

mp.figure()
mp.title('Histogram colors')
mp.xlabel('bins')
mp.ylabel('# of pixels')
mp.plot(gray_histo)
mp.xlim([0,256])
mp.show()
#color histogram

# colors=['b','g','r']

# for i,col in enumerate(colors):
#     hist=cv.calcHist([img],[i],mask,[256],[0,256])
#     # cv.imshow('Historgram Color',hist)
#     mp.plot(hist, color=col);
#     mp.xlabel([0,255])

# mp.show()


cv.waitKey(0)
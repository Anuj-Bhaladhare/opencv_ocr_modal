import cv2 as cv


image = cv.imread(r"C:\Users\kkamb\OneDrive\Desktop\code_learn\python\opencv\photos\bike.jpg");


image2 = cv.imread(r"C:\Users\kkamb\OneDrive\Desktop\code_learn\python\opencv\photos\text.png");

# cv.imshow('Cat Image',image)
gray=cv.cvtColor(image2,cv.COLOR_BGR2GRAY)


gray=cv.cvtColor(image,cv.COLOR_BGR2GRAY)
# cv.imshow('Grey Image',gray)

resize=cv.resize(gray,(200,200),100,interpolation=1);

#Simple thresholding whitescale=80 blackscale
thres, thresh_image=cv.threshold(resize,80,255,cv.THRESH_BINARY)
cv.imshow('Simple Thresholding',thresh_image)

#Inverse thresholding 
the, thresh_Inverse=cv.threshold(resize,150,255,cv.THRESH_BINARY_INV)
cv.imshow('Inverse Thresholding',thresh_Inverse)

#Adaptive thresholding
thresh_adaptive=cv.adaptiveThreshold(resize,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,15,3)
cv.imshow('Adaptive thresholding',thresh_adaptive)
thresh_adaptive=cv.adaptiveThreshold(resize,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,15,3)
cv.imshow('Adaptive thresholding mean c',thresh_adaptive)


im, threshold_text=cv.threshold(image2,100,255,cv.THRESH_BINARY_INV)
# cv.imshow('threshold text',threshold_text)


cv.waitKey(0)

import cv2 as cv


image=cv.imread(r"C:\Users\kkamb\OneDrive\Desktop\code_learn\python\opencv\photos\cat_large.jpg");

cv.imshow("image", image);

#converting image to greyscale
# grey=cv.cvtColor(image,cv.COLOR_BGR2GRAY);
# cv.imshow('GreyImage',grey);
# # grey=cv.cvtColor()

# # image2=cv.imread(r"C:\Users\kkamb\OneDrive\Desktop\code_learn\python\opencv\photos\img.jpg");
# # cv.imshow('Without Grey scale', image2);
# # gre=cv.cvtColor(image2,cv.COLOR_BGR2GRAY);

# # cv.imshow('Image2', image2);

# #blur
# blur=cv.GaussianBlur(image,(5,5),cv.BORDER_DEFAULT);
# cv.imshow('Blur', blur);

# #edge cascade
# edge=cv.Canny(blur  ,50,50);
# cv.imshow('edge cascade', edge);

# #Dialected the image
# dialect=cv.dilate(edge,(8,8), iterations=3);
# cv.imshow('dialected the image', dialect);

# #Eroding the image
# erodi=cv.erode(dialect,(5,5),iterations=2);
# cv.imshow('Eroding', erodi);

#resize image
resized = cv.resize(image, (450,550),interpolation= 5);
cv.imshow('resized image', resized);

#Cropping the image
crop=resized[50:200,200:500];
cv.imshow('CROP IMAGE',crop);





cv.waitKey(0);
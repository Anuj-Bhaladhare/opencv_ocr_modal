import cv2 as cv
# import os
# print(os.getcwd());

#reading images in python

img = cv.imread(r"C:\Users\kkamb\OneDrive\Desktop\code_learn\python\opencv\photos\cat_large.jpg");
cv.imshow('Cat',img);

cv.resize(img,(1050,1240));

cv.waitKey(0);

# print(cv.__version__);


#reading videos in python

# video =cv.VideoCapture(r"C:\Users\kkamb\OneDrive\Desktop\code_learn\python\opencv\video\video1.mp4");

# while True:
#     #read function is used to read the video
#     isTrue, frame=video.read();
#     cv.imshow('Capture', frame);
# #wait key us used to delay the closing window
#     if cv.waitKey(20) & 0xFF==ord('e'):
#         break

# video.release()
# #Destroying all the window
# cv.destroyAllWindows()
  
                           


# cv.waitKey(0);






import cv2 as cv

image = cv.imread(r"C:\Users\kkamb\OneDrive\Desktop\code_learn\python\opencv\photos\cat.jpg");

cv.imshow('cat', image);

#rescaleFrame function is used for already existing image
def rescaleFrame(frame, scale=3):
    width= int(frame.shape[1] * scale)
    height=int(frame.shape[0] * scale)
    dimension= (width, height);

    return cv.resize(frame, dimension);

resized_image= rescaleFrame(image);
cv.imshow('Image',resized_image);

cv.waitKey(0);




#liveFuction is used for the live video
def liveFunction(width,heigth):
  video.set(3,width);
  video.set(4,heigth);
   
 

# cv.waitKey(0);

#reading videos in python

video =cv.VideoCapture(r"C:\Users\kkamb\OneDrive\Desktop\code_learn\python\opencv\video\video1.mp4");

while True:
    #read function is used to read the video
    isTrue, frame=video.read();

    resized_frame=rescaleFrame(frame);

    cv.imshow('Capture', frame);
    cv.imshow('resized frame', resized_frame)
#wait key us used to delay the closing window
    if cv.waitKey(20) & 0xFF==ord('e'):
        break

video.release()
#Destroying all the window
cv.destroyAllWindows()
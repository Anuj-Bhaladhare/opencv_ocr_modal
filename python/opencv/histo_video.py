import cv2 as cv
import matplotlib.pyplot as mp
#read the content from the folder
video=cv.VideoCapture(r"C:\Users\kkamb\OneDrive\Desktop\code_learn\python\opencv\photos\human.jpg");
#imshow is used to show the video
while True:
     #read function is used to read the video
    success, cap=video.read()
    #convert this function video to gray video
    grey=cv.cvtColor(cap,cv.COLOR_BGR2GRAY);
    cv.imshow('Grey Video',grey)
    #imshow is used to show the video
    # cv.imshow('video',cap)
# calculate frequency of pixels in range 0-255
    hist_video=cv.calcHist([grey],[0],None,[256],[0,256])

    # cv.imshow('Histogram Video',cap)

    mp.figure()
    mp.title('histogram Video')
    mp.xlabel('bins')
    mp.ylabel('# number of pixels')
    mp.plot(hist_video)
    mp.xlim([0,256])
    mp.show()
    mp.close()


    if cv.waitKey(0) & 0xff == ord('c'):
        break
#  to close a video file or capturing device. 
video.release()
#Destroying all the video
cv.destroyAllWindows()


# cv.waitKey(0)
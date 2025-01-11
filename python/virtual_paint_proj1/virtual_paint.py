import cv2 as cv
import numpy as np

frameWidth=640
frameHeight=750
cap=cv.VideoCapture(0)
cap.set(3,frameWidth)
cap.set(4,frameHeight)
cap.set(10,150);

myColor=[[5,107,0,19,255,255],
         [133,56,0,159,156,255],
         [57,56,0,100,255,255]]





def findColor(img,myColor):
    imgHSV=cv.cvtColor(img,cv.COLOR_RGB2HSV)
    for color in myColor:
        lower=np.array(color[0:3])
        upper=np.array(color[3:6])
        mask=cv.inRange(imgHSV, lower, upper)
        cv.imshow(str(color[0]),mask);


def getContours(img):
    contours,hierarchy=cv.findContours(img,cv.RETR_TREE,cv.CHAIN_APPROX_NONE)

    for cnt in contours:
        area=cv.contourArea(cnt)

        if area > 500:
            cv.drawContours(imgResult, cnt, 1,(0,255,5),2)

            peri=cv.arcLength(cnt,True)

            approx=cv.approxPolyDP(cnt,0.02*peri,True)
            print(len(approx))
            




while True:
    #  print('camera sucess fully work')
     success,img=cap.read()
    #  imgGrey=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    #  cv.putText(imgGrey,'Hello Kohinoor',(100,200),cv.FONT_HERSHEY_PLAIN,1.0,(0,0,255),3)
     findColor(img,myColor)
     cv.imshow("Video",img)

     if cv.waitKey(1) & 0xff == ord("c"):
        break
                                   


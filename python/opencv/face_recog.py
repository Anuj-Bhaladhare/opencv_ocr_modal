import cv2 as cv
import numpy as np
#load the haarscascade file
cascade_image=cv.CascadeClassifier(r'C:\Users\kkamb\OneDrive\Desktop\code_learn\python\opencv\haarcascade_frontalface_default.xml')

list1=['elon musk','Narendra modi']

#load the feature and labels
features=np.load('features.npy')
labels=np.load('labels.npy')
#Creates an Local Binary Pattern Histogram face recognizer.
face_recognition=cv.face.LBPHFaceRecognizer_create()
#reads the trained model
face_recognition.read('face_trained.yml');

image=cv.imread(r'C:\Users\kkamb\OneDrive\Desktop\code_learn\python\opencv\faces\elon musk\elon_musk4.jpg')
# print(image)

#convert into the gray scale image
gray=cv.cvtColor(image,cv.COLOR_BGR2GRAY)
cv.imshow('Gray image',gray)
cascade_image=cv.CascadeClassifier(r'C:\Users\kkamb\OneDrive\Desktop\code_learn\python\opencv\haarcascade_frontalface_default.xml')
        
#Detect the face
face_detect=cascade_image.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=5)

for (x,y,w,h) in face_detect:
      #Crops the detected face from the grayscale image using the coordinates and dimensions 
      face_roi=gray[y:y+h,x:x+h]


      label, confidence=face_recognition.predict(face_roi)
      print(f'Label={list1[label]} with a confidence of {confidence}')

      cv.putText(gray,str(list1[label]),(20,20),cv.FONT_HERSHEY_COMPLEX,1.0,(0,255,0),thickness=2)

      cv.rectangle(gray,(x,y),(x+w,y+h),(0,255,0),thickness=3)

cv.imshow('Gray image',gray)
cv.waitKey(0)
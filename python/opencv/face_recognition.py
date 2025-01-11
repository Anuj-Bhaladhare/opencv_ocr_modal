import cv2 as cv
import numpy as np
import os


list1=['elon musk','Narendra modi']
print(list1)
dir= r'C:\Users\kkamb\OneDrive\Desktop\code_learn\python\opencv\faces'

features=[]
labels=[]

def create_train():
    #for finding  directory of a person
    for person in list1:
        path=os.path.join(dir,person)
        label=list1.index(person)
     #for finding the image directory in the folder
        for image in os.listdir(path):
            image_path=os.path.join(path, image)

            #image into the grayscle for image process
            img_array=cv.imread(image_path)
            gray=cv.cvtColor(img_array,cv.COLOR_BGR2GRAY)
#load the haarscade
    cascade_image=cv.CascadeClassifier(r'C:\Users\kkamb\OneDrive\Desktop\code_learn\python\opencv\haarcascade_frontalface_default.xml')
        
#detect the face
    face_detect=cascade_image.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=3)

   # to crop the image face
    for (x,y,w,h) in face_detect:
        face_roi=gray[y:y+h,x:x+h]
        features.append(face_roi)
        labels.append(label)

#call the function
create_train()

print(f'length of the label: {len(labels)}')

print(f'length of the features: {len(features)}')

features=np.array(features)
labels=np.array(labels)
face_recognition=cv.face.LBPHFaceRecognizer_create()
#train the recognizer of giving labels and features list
face_recognition.train(features,labels)

face_recognition.save('face_trained.yml')
np.save('features.npy',features)
np.save('labels.npy',labels)
#another way to extract list from the folder 
# person=[]

# for i in os.listdir(r'C:\Users\kkamb\OneDrive\Desktop\code_learn\python\opencv\faces'):
#     person.append(i)

# print(person)
import cv2 as cv

cap=cv.VideoCapture(0)

while True:
    success, frame=cap.read()
    cv.imshow('Frame',frame)
#convert into grey
    grey=cv.cvtColor(frame,cv.COLOR_BGR2GRAY);
    cv.imshow('Grey',grey)

#load the hashcascade
    cascade_image=cv.CascadeClassifier(r'C:\Users\kkamb\OneDrive\Desktop\code_learn\python\opencv\haarcascade_frontalface_default.xml')

 #detect the face
    face_detect=cascade_image.detectMultiScale(grey,scaleFactor=1.1,minNeighbors=3,minSize=(50,50))
    # print(f'The number of faces {len(face_detect)} ')
    # cv.imshow('Face Detected',face_detect)

 #make a rectangle on image face
 #for loop detecting the faces
    for (x,y,w,h) in face_detect:
        # (x, y): The starting point of the rectangle (top-left corner).
        # (x + w, y + h): The ending point of the rectangle (bottom-right corner).
        # (0, 255, 0): green color for the rectangle.
        # 3: Thickness of the rectangle's border.
        face=cv.rectangle(grey,(x,y),(x+w,y+h),(0,255,0),thickness=3)
       #f is  a formatted string.
        image=f'number of face detect: {len(face_detect)}'
        #grey is input image,
        text=cv.putText(grey,image,(50,50),cv.FONT_HERSHEY_SIMPLEX,1,255,2)
    
    cv.imshow('DETECT FACE',grey)

         
    

    key=cv.waitKey(200) 
    if key == ord('c'):
        break
  #: Releases the video capture object.  
frame.release()
cv.destroyAllWindows()
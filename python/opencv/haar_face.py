import cv2 as cv

image=cv.imread(r"C:\Users\kkamb\OneDrive\Desktop\code_learn\python\opencv\photos\front.jpg")

#convert to grey scale
gray=cv.cvtColor(image,cv.COLOR_BGR2GRAY)
cv.imshow("Gray",gray)
#load the cascade
cascade_image=cv.CascadeClassifier(r'C:\Users\kkamb\OneDrive\Desktop\code_learn\python\opencv\haarcascade_frontalface_default.xml')

# resize=cv.resize(gray,(500,500))
# cv.imshow('Resized image',resize)
#detect the faces
#gray is a input image, 
# scaleFactor: Specifies how much the image size is reduced at each image scale.
# minNeighbors: Specifies how many neighbors each candidate rectangle should have to retain it.
# minSize: Minimum possible object size. Objects smaller than this are ignored
faces=cascade_image.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=1)
print(f'Number of faces {len(faces)}')


#draw a rectangle around the faces
#image is a input image
# (x, y): The starting point of the rectangle (top-left corner).
# (x + w, y + h): The ending point of the rectangle (bottom-right corner).
# (255, 0, 0): Blue color for the rectangle.
# 3: Thickness of the rectangle's border.
for (x,y,w,h) in faces:
    rectangle=cv.rectangle(gray,(x,y),(x+w,y+h),(0,220,255),3)


cv.imshow('faces',gray)

# cv.imshow('Image',image)
cv.waitKey(0)
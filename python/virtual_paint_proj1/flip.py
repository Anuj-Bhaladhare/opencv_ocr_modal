import cv2 as cv
import os

cap=cv.VideoCapture(0)

while True:
    success, img=cap.read()
    cv.imshow('Press "c" to caputre, "q" to quit', img)
    key=cv.waitKey(1) & 0xff
    if key == ord('c'):
        save_dir='capture_image'
        photo_path= os.makedirs(save_dir,exist_ok=True)
        cv.imwrite(photo_path,img)
        # cv.imwrite('st.jpg',img);
        print('photo saved successfully')
        break
    elif key == ord('q'):
       break
    else:
        print('error')

cap.release()
cv.destroyAllWindows()

image=cv.imread(photo_path)
cv.imshow('Image show',image)

#rotate the image 90degree
rotate_Image=cv.rotate(image,cv.ROTATE_90_CLOCKWISE)
cv.imshow('Rotated image',rotate_Image);
cv.imwrite('rotated_image.jpg',rotate_Image);

cv.waitKey(0)



    



        

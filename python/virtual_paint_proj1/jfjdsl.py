import cv2
import numpy as np

cam = cv2.VideoCapture(0)
while True:
    ret, frame = cam.read()
    cv2.imshow('Press "c" to capture, "q" to quit', frame)
    key = cv2.waitKey(1) & 0xFF
    if key == ord('c'):
        cv2.imwrite('temp_photo.jpg', frame)
        image = cv2.imread('temp_photo.jpg')
        (h, w) = image.shape[:2]
        if h > w:
            M = cv2.getRotationMatrix2D((w // 2, h // 2), -90, 1.0)
            rotated_image = cv2.warpAffine(image, M, (w, h))
            cv2.imwrite('rotated_photo.jpg', rotated_image)
            print('Final image saved as: rotated_photo.jpg')
        else:
            print('Final image saved as: temp_photo.jpg')
        break
    elif key == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
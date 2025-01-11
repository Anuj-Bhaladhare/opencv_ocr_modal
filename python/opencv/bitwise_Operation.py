import cv2 as cv
import numpy as np

blank=np.zeros((500,500), dtype='uint8')

rectangle=cv.rectangle(blank.copy(),(20,20),(300,300),255,-1)
circle=cv.circle(blank.copy(),(300,300),50,255,-1)
cv.imshow('Circle',circle)
cv.imshow('Rectangle',rectangle)

#bitwise and -->intersecting region
bitwise_and=cv.bitwise_and(rectangle,circle);
cv.imshow('Bitwise and',bitwise_and);

#bitwise or -->non-intersecting region and intersecting region
bitwise_or=cv.bitwise_or(rectangle,circle);
cv.imshow('Bitwise or', bitwise_or)

#bitwise xor -->non-intersecting region
bitwise_xor=cv.bitwise_xor(rectangle,circle);
cv.imshow('Bitwise xor',bitwise_xor);

#bitwise not -->invert the image
# mask=np.zeros(rectangle.shape[250:152,154:250],dtype='uint8');
bitwise_not=cv.bitwise_not(circle);
cv.imshow('Bitwise not',bitwise_not);


# cv.imshow('Blank',blank)
cv.waitKey(0)
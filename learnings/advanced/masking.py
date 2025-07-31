import cv2 as cv
import numpy as np

img = cv.imread('../photos/cats 2.jpg')
cv.imshow('Cats', img)

# Masking helps in removing unwanted parts of the image by masking people faces.
blank = np.zeros(img.shape[:2], dtype='uint8') # Note: The dimensions of the image must be of same size as the original image
cv.imshow('Blank', blank)

circle = cv.circle(blank.copy(), (img.shape[1]//2 + 45,img.shape[0]//2), 100, 255, -1)
cv.imshow('Circle', circle)

# rectangle_mask = cv.rectangle(blank, (img.shape[1]//2,img.shape[0]//2), (img.shape[1]//2 + 100,img.shape[0]//2 + 100), 255, -1)
# cv.imshow('Rectangle', rectangle_mask)

rectangle = cv.rectangle(blank.copy(), (30,30), (370,370), 255, -1)
weird_shape = cv.bitwise_and(circle, rectangle)
cv.imshow('Weird shape', weird_shape)

masked = cv.bitwise_and(img, img, mask=weird_shape)
cv.imshow('Weird shape masked Image', masked)


cv.waitKey(0)
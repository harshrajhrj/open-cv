import cv2 as cv
import numpy as np

img=cv.imread('../photos/boston.jpg')
cv.imshow('Boston', img)

b,g,r = cv.split(img)
# cv.imshow('Blue', b)
# cv.imshow('Green', g)
# cv.imshow('Red', r)

print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

# Merge channels
merged = cv.merge([b,g,r])
cv.imshow('Merged Image', merged)

# Way to visualize actual color in each channel
blank = np.zeros(img.shape[:2], dtype='uint8')

blue = cv.merge([b,blank,blank])
green = cv.merge([blank,g,blank])
red = cv.merge([blank,blank,r])

cv.imshow('Blue', blue)
cv.imshow('Green', green)
cv.imshow('Red', red)

cv.waitKey(0)
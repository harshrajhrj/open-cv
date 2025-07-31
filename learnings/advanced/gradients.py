import cv2 as cv
import numpy as np

img = cv.imread('../photos/cats.jpg')
cv.imshow('Cats', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# We can think of gradients are like edge-like regions present in image but they're not the same thing.

# Laplacian
lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap)) # Since pixel values can't be negative hence we make them positive by apply np.absolute() and converting to image format i.e. uint8
cv.imshow('Laplacian', lap)

# Sobel
# Sobel filter calculates gradients in two directions: x and y axis
sobelX = cv.Sobel(gray, cv.CV_64F, 1, 0)
sobelY = cv.Sobel(gray, cv.CV_64F, 0, 1)
combined_sobel = cv.bitwise_or(sobelX, sobelY)

cv.imshow('SobelX', sobelX)
cv.imshow('SobelY',sobelY)
cv.imshow('Combined Sobel', combined_sobel)

canny = cv.Canny(gray, 150, 255)
cv.imshow('Canny', canny) # Multi-stage process in which sobel is also used

cv.waitKey(0)
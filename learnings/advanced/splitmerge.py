import cv2 as cv
import numpy as np

img= cv.imread('..photos/boston.jpg')
cv.imshow('Boston', img)


cv.waitKey(0)
import cv2 as cv
import numpy as np

img = cv.imread('../photos/cats.jpg')

cv.imshow('Cats', img)


blank = np.zeros(img.shape, dtype='uint8')
cv.imshow('Blank', blank)

# Contours are basically the boundaries of an object, the line or curve that joins continuous points along the boundaries of an object.
# From a mathematical point of view, they are different from edges. Contours are useful when we do shape analysis and object detection and recognition

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)
# cv.imshow('Blur', blur)

# canny edge detector
# canny = cv.Canny(blur, 125, 175)
# cv.imshow('Canny Edges', canny)

# contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
# contours returns list of elements which are true for all the found contours
# hierarchies: example a rectangle, inside rect. a square, inside square a circle
# cv.RETR_LIST returns all the contours defined in the image
# cv.RETR_TREE returns all the hierarchical systems
# cv.CHAIN_APPROX_NONE doesn't make any approximation, cv.CHAIN_APPROX_SIMPLE approximates/compresses the contours how it looks. Example: CHAIN_APPROX_NONE
# would have returned all the coordinates of a line (for contour detection) but CHAIN_APPROX_SIMPLE returns only two coordinates (representation of a line) 
# instead of return of the coordinates of the line
# print(f'{len(contours)} contour(s) found!')

# contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
# print(f'{len(contours)} contour(s) found!')

# Instead of using canny edge detector we can use threshold
ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY) # binarize the image, below 125 pixel set to '0' and above 125 set to '255'
cv.imshow('Thresh', thresh)

contours, hierarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contour(s) found!')

# we can visualize the contours that were found by essentally drawing on the image
# draw contours on the blank image to find out what contours have been found
# we want all the contours on the blank image so we mention "-1"
cv.drawContours(blank, contours, -1, (0,0,255), thickness=1)
cv.imshow('Contnours drawn', blank)

cv.waitKey(0)
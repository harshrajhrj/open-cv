import cv2 as cv
import numpy as np

# giving a shape of height, width, channel
blank = np.zeros((500, 500, 3), dtype='uint8')
# cv.imshow('Blank', blank)


# img = cv.imread('../photos/cat.jpg')
# cv.imshow('Cat', img)

# there two ways to draw an image
# 1. to draw on standalone image
# 2. to create a dummy/blank image

# 1. Paint the image a certain color
# [:] reference all cells
# blank[:]=0,255,0 # painting an entire image green
# cv.imshow('Green', blank)

# blank[:]=0,0,255 # painting an entire image red
# cv.imshow('Red', blank)

# drawing a certain shape
# blank[200:300, 300:400] = 0,0,255
# cv.imshow('Green', blank)

# 2. Draw a rectangle
# cv.rectangle(blank, (0,0), (250, 250), (0, 255, 0), thickness=2)
# cv.imshow('Rectangle', blank)

# or fill the rectangle by changing the thickness using cv.FILLED or -1
# cv.rectangle(blank, (0,0), (250, 500), (0,255,0), thickness=-1)
# cv.imshow('Rectangle_filled', blank)

# or instead of mentioning the shapes, we can use "np.shape()" method
# cv.rectangle(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (0,255,0), thickness=-1)
# cv.imshow('Rectangle', blank)

# 3. Draw a circle
# cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0,0,255), thickness=3)
# cv.imshow('Circle', blank)

# cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0,0,255), thickness=-1)
# cv.imshow('Circle_filled', blank)

# 4. Draw a line
# cv.line(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (255,255,255), thickness=3)
# cv.imshow('Line', blank)

# cv.line(blank, (100,250), (300, 400), (255,255,255), thickness=3)
# cv.imshow('Line', blank)

# 5. Write text
# cv.putText(blank, 'Hello', (255,255), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0), 2)
# cv.imshow('Text', blank)

# for a large text we can adjust the margins
cv.putText(blank, 'Hello, my name is Harsh Raj', (0, 255), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0), thickness=2)
cv.imshow('Text', blank)

cv.waitKey(0)
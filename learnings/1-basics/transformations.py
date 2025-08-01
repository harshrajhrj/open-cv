import cv2 as cv
import numpy as np

img = cv.imread('../photos/boston.jpg')
cv.imshow('Boston', img)

# Translations
# Shifting the image up, down, left, right along x-y axis

def translate(img, x, y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)

# -x -> left
# -y -> up
# x -> right
# y -> down

# translated = translate(img, 100, 100) # shift image right by 100 pixels and down by 100 pixels
# cv.imshow('Translated Right Down', translated)

# translated = translate(img, -100, 100) # shift image left by 100 pixels and down by 100 pixels
# cv.imshow('Translated Left Down', translated)


# Rotation
# By default: rotation around centered point
def rotate(img, angle, rotPoint=None):
    (height, width) = img.shape[:2]
    
    if rotPoint is None: # rotate about center
        rotPoint = (width//2, height//2)
    
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0) # WE DON'T WANT TO SCALE SO KEEP IT "1.0"
    dimensions = (width,height)

    return cv.warpAffine(img, rotMat, dimensions)


# rotated = rotate(img, 45) # anti-clockwise
# rotated = rotate(img, -45) # clockwise
# cv.imshow('Rotated', rotated)

# rotated_rotated = rotate(rotated, -45) # clockwise
# The reason we get some parts of black traingle because the second rotation also follows the triangle that were the part of first rotation
# cv.imshow('Rotated rotated', rotated_rotated)

# rotated_rotated = rotate(img, -90) # clockwise
# cv.imshow('Rotated rotated', rotated_rotated)


# Resizing
# resized = cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC) # cv.INTER_CUBIC is a little slower
# cv.imshow('Resized', resized)

# Flipping
flip = cv.flip(img, 1) # flip code can be 0,1,-1....."0" flipping the image vertically, "1" flip the image horizontally or over y-axis, "-1" both vertically and horizontally
cv.imshow('Flip', flip)

# Cropping
cropped = img[200:400, 300:400]
cv.imshow('Cropped', cropped)

cv.waitKey(0)
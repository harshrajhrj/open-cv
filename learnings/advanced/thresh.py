import cv2 as cv

img = cv.imread('../photos/cats.jpg')
cv.imshow('Cats', img)

# Thresholding is the binarization of the image where pixels are either 0 (black) or 255 (white)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Simple thresholding
threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
cv.imshow('Simple Thresholded', thresh)

# Inverse
threshold, thresh_inv = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)
cv.imshow('Simple Thresholded Inverse', thresh_inv)

# Adaptive Thresholding
# Let the algorithm find the optimal thresholding value by itself (downside of simple thresholding)
# @param: adaptiveMethod (kernel type)
# @param: thresholdType
# @kernelSize: 11
# @c: to find tune the mean value (will be subtracted)
# adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 3)
adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 3)
cv.imshow('Adaptive Thresholding', adaptive_thresh)

cv.waitKey(0)
import cv2 as cv

img = cv.imread('../photos/cat.jpg')

cv.imshow('Image', img)

# converting an image to grayscale: we can see the intensity of color distribution rather than pixels
# gray=cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray', gray)

# blur : essentially remove some of the noises that exist in image
# ksize has to be an odd number
# blur = cv.GaussianBlur(img, (3,3), cv.BORDER_DEFAULT)
# cv.imshow('Blur', blur)

# blur can be increased by increasing the kernel size
# blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
# cv.imshow('Increased Blur', blur)

# Edge cascade: trying to find the edges that are present in the image. The famous one is canny edge detector
# canny = cv.Canny(img, 125, 175)
# cv.imshow('Canny', canny)

# we can reduce the number of edges by applying blur to the image
# canny = cv.Canny(blur, 125, 175)
# cv.imshow('Canny edges', canny)

# Dilating the image
# how to dilate an image using structuring element: these elements can be canny edges that we have found
# dilated = cv.dilate(canny, (7,7), iterations=3)
# cv.imshow('Dilated', dilated)

# Eroding: restoring the canny edge after dilating
# eroded = cv.erode(dilated, (7,7), iterations=3)
# cv.imshow('Eroded', eroded)

# Resize
resized = cv.resize(img, (500, 500)) # ignoring the aspect ratio
cv.imshow('Resized Image', resized)

# Adding interpolation in the background to the image that are smaller in dimensions compared to the original image
resized_interpolation = cv.resize(img, (500, 500), interpolation=cv.INTER_AREA)
cv.imshow('Resized Image Interpolation', resized_interpolation)
# Incase of enlarging or scaling the image, we use cv.INTER_CUBIC or cv.INTER_LINEAR to get much higher quality

# Cropping
cropped = img[50:200, 200:400]
cv.imshow('Cropped', cropped)

cv.waitKey(0)
import cv2 as cv

img = cv.imread('../photos/cats.jpg')
cv.imshow('Cats',img)

# We generally smooth an image when there is a lot of noise by applying some blurring method.

# Averaging
average = cv.blur(img, (3,3))
cv.imshow('Average', average)

# Gaussian
# @param: Standard deviation in x-direction
gauss = cv.GaussianBlur(img, (3,3), 0)
cv.imshow('Gaussian', gauss)

# Median: It tends to be more effective in removing noise from an image as compared to Average and Gaussian blur.
# It pretty good at removing some salt and pepper noise that exists in the image.
# Median blurring is not meant for high kernel sizes
medianBlur = cv.medianBlur(img, 3)
cv.imshow('Median', medianBlur)

# Bilateral Blur
# Blurring retains the image as well
# https://docs.opencv.org/4.x/d4/d86/group__imgproc__filter.html#ga9d7064d478c95d60003cf839430737ed
bilateral = cv.bilateralFilter(img, 5, 150, 150)
cv.imshow('Bilateral', bilateral)

cv.waitKey(0)
import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('../photos/boston.jpg')
cv.imshow('Boston', img) # opencv displays BGR image

# plt.imshow(img) # matplotlib has no idea whether the image is BGR or RGB
# plt.show() # displayed in BGR (inversion of colors)

# Switching between color spaces in opencv
# A space of colors. A system of representing an array of pixel colors. RGB, Grayscale, HSV, LAB, etc manymore

# BGR to Grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# BGR to HSV (Hue Saturation Value) How humans think and perceive color
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV', hsv)

# BGR to LAB
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('LAB', lab) # WASHED OUT BGR image, similar to how human perceive color

# BGR to RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('RGB', rgb)

# we cannot directly convert hsv to grayscale. Process is HSV to BGR then BGR to Grayscale
hsv_bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
cv.imshow('HSV --> BGR', hsv_bgr)

# plt.imshow(rgb) # displays RGB
# plt.show()

cv.waitKey(0)
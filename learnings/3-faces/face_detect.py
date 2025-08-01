import cv2 as cv

img = cv.imread('../photos/group 1.jpg')
cv.imshow('Person', img)

# Face detection detects the presence of a face in an image. It is performed using a classifier. A classifier is essentially an algorithm that decides whether an image
# is positive or negative whether a face is present or not. It has to be trained with 10's of 1000 images. opencv comes with pre-trained classifiers that can be used in
# any program. The two main classifiers that exist today is: haar_cascades and local binary pattern.

# Convert to grascale. Face detection doesn't involve skin tone or colors inside an image. It looks for the edges in the image and detects an object.
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

haar_cascade = cv.CascadeClassifier('haar_face.xml')

# @param: minNeighbors i.e. number of rectangles that should have to be called a face
faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3) # returns rectangular coordinates as a list to that of faces detected

print(f'Number of faces found = {len(faces_rect)}')

for (x,y,w,h) in faces_rect:
    cv.rectangle(img, (x,y), (x+w,y+h), (0,255,0), thickness=2)

cv.imshow('Detected Faces', img) # Prone to noises

# Face recognition involves identifying whose face it is.


cv.waitKey(0)
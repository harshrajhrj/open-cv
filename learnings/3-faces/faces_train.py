import os
import cv2 as cv
import numpy as np

people = ['Jerry Seinfield', 'Elton John', 'Ben Afflek', 'Madonna', 'Mindy Kaling']

haar_cascade = cv.CascadeClassifier('haar_face.xml')

# p = []
# for i in os.listdir(r'Faces/train/'):
#     p.append(i)

# print(p)

DIR = r'Faces/train/'

# Training set
features = [] # image array of faces
labels = [] # corresponding label or whose face it belongs to
def create_train():
    for person in people:
        path = os.path.join(DIR, person)
        label = people.index(person)

        for img in os.listdir(path):
            img_path = os.path.join(path, img)

            img_array = cv.imread(img_path)

            if img_array is None:
                continue

            gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)

            # detect faces in the image
            faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)

            for(x,y,w,h) in faces_rect:
                faces_roi = gray[y:y+h, x:x+w] # crop faces to get the regions of interest
                features.append(faces_roi)
                labels.append(label)


create_train()

# print(f'Length of the features = {len(features)}')
# print(f'Length of the labels = {len(labels)}')

print('Training done ------------')

features = np.array(features, dtype='object')
labels = np.array(labels)

face_recognizer = cv.face.LBPHFaceRecognizer_create()

# Train the recognizer on the features list and the labels list
face_recognizer.train(features, labels)

# To overcome repetition of above steps, we will save the trained model to load it anywhere
face_recognizer.save('face_trained.yml')
np.save('features.npy', features)
np.save('labels.npy', labels)
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 10:08:58 2022

@author: atman
"""
import numpy as np
import cv2

def blur_face(img):
    (h, w) = img.shape[:2]
    dW = int(w / 3.0)
    dH = int(h / 3.0)
    if dW % 2 == 0:
        dW -= 1
    if dH % 2 == 0:
        dH -= 1
    return cv2.GaussianBlur(img, (dW, dH), 0)


# string = cv2.videoio_registry.getBackendName(0)
# print(string)
capture = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier('F:\GitHub\OpenCV_4\opencv\data\haarcascades\haarcascade_frontalface_default.xml')

if not capture.isOpened():
    print("Cannot open camera")
    exit()

while True:
    ret, img = capture.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    faces = face_cascade.detectMultiScale(img, scaleFactor=2, minNeighbors=5, minSize=(30, 30))
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        img[y:y + h, x:x + w] = blur_face(img[y:y + h, x:x + w])

    cv2.imshow('From Camera', img)
    k = cv2.waitKey(30) & 0xFF
    if k == 27:
        break

capture.release()
cv2.destroyAllWindows()

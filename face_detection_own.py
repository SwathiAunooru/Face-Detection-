# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 11:30:38 2019

@author: swathi
"""
import cv2
import sys
import numpy as np

cap = cv2.VideoCapture(0)
while True:
    ret,image = cap.read()
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.3,
        minNeighbors=3,
        minSize=(30, 30)
    )
    
    print("[INFO] Found {0} Faces!".format(len(faces)))
    
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(image, "face", (x, y),
			cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 0, 255), 2)


    cv2.imshow("Frame", image)
    key = cv2.waitKey(1) & 0xFF
    
#    status = cv2.imwrite('faces_detected.jpg', image)
#    print("[INFO] Image faces_detected.jpg written to filesystem: ", status)
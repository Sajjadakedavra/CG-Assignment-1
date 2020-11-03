# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 22:38:55 2020

@author: Sajjad
"""

import cv2
import sys
  
#image = cv2.imread(r'E:\sajjad university\6th semester\computer graphics\jurassic-park-tour-jeep.jpg')
#gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
  
#cv2.imshow('Original image',image)
#cv2.imshow('Gray image', gray)
  
#cv2.waitKey(0)
#cv2.destroyAllWindows()


def faceDetectAndAlterProps():

    # Get user supplied values
    imagePath = r"E:\sajjad university\6th semester\computer graphics\abba.png"
    cascPath = r"E:\sajjad university\6th semester\computer graphics\haarcascade_frontalface_default.xml"
    
    # Create the haar cascade
    faceCascade = cv2.CascadeClassifier(cascPath)
    
    # Read the image
    image = cv2.imread(imagePath)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Detect faces in the image
    #.detectMultiscale detects the objects on our cascade
    #first option is the grayscale image
    #scaleFactor compensates for difference in distances between faces and camera
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        #flags = cv2.cv.CV_HAAR_SCALE_IMAGE
    )
    
    print("Found {0} faces!".format(len(faces)))
    
    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
    
    cv2.imshow("Faces found", image)
    cv2.imwrite(r'E:\sajjad university\6th semester\computer graphics\binaryToGrayAndFaceDetection\try.png', image)
    print("---------")
    cv2.waitKey(0)
    
faceDetectAndAlterProps()
    
    
    
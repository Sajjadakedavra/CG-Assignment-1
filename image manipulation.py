# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 13:48:45 2020

@author: Sajjad
"""

import cv2

image = cv2.imread("jurassic-park-tour-jeep.jpg")
cv2.imshow("original", image)
cv2.waitKey(0)

cropped = image[70:270, 440:640]    #startY endY startX endX coordinates. the biiger the difference, less cropped the image
cv2.imshow("cropped", cropped)
cv2.waitKey(0)
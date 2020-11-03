# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 22:38:55 2020

@author: Sajjad
"""

import cv2
  
image = cv2.imread(r'E:\sajjad university\6th semester\computer graphics\jurassic-park-tour-jeep.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
  
cv2.imshow('Original image',image)
cv2.imshow('Gray image', gray)
  
cv2.waitKey(0)
cv2.destroyAllWindows()
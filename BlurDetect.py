# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 20:36:10 2020

@author: atman
"""


import cv2
import numpy as np
# import scipy as sp


imgIn = cv2.imread('c:/images/girl.jpg', cv2.IMREAD_GRAYSCALE) 
cv2.imwrite('c:/images/grayorig.jpg', imgIn)
height, width = imgIn.shape[:2]
imgOut = np.zeros((height,width), np.uint8)
imgTemp = np.zeros((height,width), np.uint8)

imgTemp = cv2.Laplacian(imgIn, 8, 1)
imgOut = imgIn - imgTemp

cv2.imshow("Laplas", imgOut)
cv2.waitKey(0)
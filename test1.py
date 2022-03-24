# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 12:53:28 2020

@author: atman
"""

import cv2

def loading_displaying_saving():
    img = cv2.imread('c:/images/girl.jpg', cv2.IMREAD_GRAYSCALE)
    cv2.imshow('girl', img)
    cv2.waitKey(0)
    cv2.imwrite('c:/images/graygirl.jpg', img)
    print("Высота:"+str(img.shape[0]))
    print("Ширина:" + str(img.shape[1]))
    print("Количество каналов:" + str(img.shape[2]))
    
loading_displaying_saving()    
    
    
    
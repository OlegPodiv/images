# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 14:35:45 2020

@author: atman
"""

import cv2 
import numpy as np
# import scipy as sp

Kx3 = np.array([-1, 0, 1,
                -1, 0, 1,
                -1, 0, 1], float)

Ky3 = np.array([-1, -1, -1,
                 0,  0,  0,
                 1,  1,  1], float)

Kx5 = np.array([-1, -1,  0,  1,  1,
                -1, -1,  0,  1,  1,
                -1, -1,  0,  1,  1,
                -1, -1,  0,  1,  1,
                -1, -1,  0,  1,  1], float)

Ky5 = np.array([-1, -1, -1, -1, -1,
                -1, -1, -1, -1, -1,
                 0,  0,  0,  0,  0,
                 1,  1,  1,  1,  1,
                 1,  1,  1,  1,  1], float)

Kx7 = np.array([-1, -1, -1,  0,  1,  1,  1,
                -1, -1, -1,  0,  1,  1,  1,
                -1, -1, -1,  0,  1,  1,  1,
                -1, -1, -1,  0,  1,  1,  1,
                -1, -1, -1,  0,  1,  1,  1,
                -1, -1, -1,  0,  1,  1,  1,
                -1, -1, -1,  0,  1,  1,  1], float)

Ky7 = np.array([-1, -1, -1, -1, -1, -1, -1,
                -1, -1, -1, -1, -1, -1, -1,
                -1, -1, -1, -1, -1, -1, -1,
                 0,  0,  0,  0,  0,  0,  0,
                 1,  1,  1,  1,  1,  1,  1,
                 1,  1,  1,  1,  1,  1,  1,
                 1,  1,  1,  1,  1,  1,  1], float)

Kx9 = np.array([-1, -1, -1, -1,  0,  1,  1,  1,  1,
                -1, -1, -1, -1,  0,  1,  1,  1,  1,
                -1, -1, -1, -1,  0,  1,  1,  1,  1,
                -1, -1, -1, -1,  0,  1,  1,  1,  1,
                -1, -1, -1, -1,  0,  1,  1,  1,  1,
                -1, -1, -1, -1,  0,  1,  1,  1,  1,
                -1, -1, -1, -1,  0,  1,  1,  1,  1,
                -1, -1, -1, -1,  0,  1,  1,  1,  1,
                -1, -1, -1, -1,  0,  1,  1,  1,  1], float)

Ky9 = np.array([-1, -1, -1, -1, -1, -1, -1, -1, -1,
                -1, -1, -1, -1, -1, -1, -1, -1, -1,
                -1, -1, -1, -1, -1, -1, -1, -1, -1,
                -1, -1, -1, -1, -1, -1, -1, -1, -1,
                 0,  0,  0,  0,  0,  0,  0,  0,  0,
                 1,  1,  1,  1,  1,  1,  1,  1,  1,
                 1,  1,  1,  1,  1,  1,  1,  1,  1,
                 1,  1,  1,  1,  1,  1,  1,  1,  1,
                 1,  1,  1,  1,  1,  1,  1,  1,  1], float)

Kx11 = np.array([-1, -1, -1, -1, -1,  0,  1,  1,  1,  1,  1,
                 -1, -1, -1, -1, -1,  0,  1,  1,  1,  1,  1,
                 -1, -1, -1, -1, -1,  0,  1,  1,  1,  1,  1,
                 -1, -1, -1, -1, -1,  0,  1,  1,  1,  1,  1,
                 -1, -1, -1, -1, -1,  0,  1,  1,  1,  1,  1,
                 -1, -1, -1, -1, -1,  0,  1,  1,  1,  1,  1,
                 -1, -1, -1, -1, -1,  0,  1,  1,  1,  1,  1,
                 -1, -1, -1, -1, -1,  0,  1,  1,  1,  1,  1,
                 -1, -1, -1, -1, -1,  0,  1,  1,  1,  1,  1,
                 -1, -1, -1, -1, -1,  0,  1,  1,  1,  1,  1,
                 -1, -1, -1, -1, -1,  0,  1,  1,  1,  1,  1], float)

Ky11 = np.array([-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
                 -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
                 -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
                 -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
                 -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
                  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
                  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,
                  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,
                  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,
                  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,
                  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1], float)
# ------------------------------------------------------------------------
imgIn = cv2.imread('f:/images/nomer.png', cv2.IMREAD_GRAYSCALE) 
cv2.imwrite('f:/images/graynomer.jpg', imgIn)
height, width = imgIn.shape[:2]
imgOut = np.zeros((height,width), float)
imgTemp = np.zeros((height,width), float)
imgTemp = 256*imgIn

# 1-----------------------------------------------------------------------
Rx3 = cv2.filter2D(imgTemp, -1, Kx3)/6.
Ry3 = cv2.filter2D(imgTemp, -1, Ky3)/6.

Rx5 = cv2.filter2D(imgTemp, -1, Kx5)/30.
Ry5 = cv2.filter2D(imgTemp, -1, Ky5)/30.

Rx7 = cv2.filter2D(imgTemp, -1, Kx7)/84.
Ry7 = cv2.filter2D(imgTemp, -1, Ky7)/84.

Rx9 = cv2.filter2D(imgTemp, -1, Kx9)/180.
Ry9 = cv2.filter2D(imgTemp, -1, Ky9)/180.

Rx11 = cv2.filter2D(imgTemp, -1, Kx11)/330.
Ry11 = cv2.filter2D(imgTemp, -1, Ky11)/330.

# 2------------------------------------------------------------------------
Px3 = np.zeros((height,width), float)
Px5 = np.zeros((height,width), float)
Px7 = np.zeros((height,width), float)
Px9 = np.zeros((height,width), float)
Px11 = np.zeros((height,width), float)
Py3 = np.zeros((height,width), float)
Py5 = np.zeros((height,width), float)
Py7 = np.zeros((height,width), float)
Py9 = np.zeros((height,width), float)
Py11 = np.zeros((height,width), float)

for i in range(1, height-1) :
    for j in range(1, width-1):
        Px3[i,j] = (Rx3[i,j+1] - Rx3[i,j-1])/2
        Py3[i,j] = (Ry3[i+1,j] - Ry3[i-1,j])/2
        
        Px5[i,j] = (Rx5[i,j+1] - Rx5[i,j-1])/2
        Py5[i,j] = (Ry5[i+1,j] - Ry5[i-1,j])/2
        
        Px7[i,j] = (Rx7[i,j+1] - Rx7[i,j-1])/2
        Py7[i,j] = (Ry7[i+1,j] - Ry7[i-1,j])/2
        
        Px9[i,j] = (Rx9[i,j+1] - Rx9[i,j-1])/2
        Py9[i,j] = (Ry9[i+1,j] - Ry9[i-1,j])/2
        
        Px11[i,j] = (Rx11[i,j+1] - Rx11[i,j-1])/2
        Py11[i,j] = (Ry11[i+1,j] - Ry11[i-1,j])/2
        
# 3-----------------------------------------------------------------------
_Rx3 = np.zeros((height,width), float)
_Rx5 = np.zeros((height,width), float)
_Rx7 = np.zeros((height,width), float)
_Rx9 = np.zeros((height,width), float)
_Rx11 = np.zeros((height,width), float)
_Ry3 = np.zeros((height,width), float)
_Ry5 = np.zeros((height,width), float)
_Ry7 = np.zeros((height,width), float)
_Ry9 = np.zeros((height,width), float)
_Ry11 = np.zeros((height,width), float)

for i in range(3, height-3) :
    for j in range(3, width-3):        
        k = int(3 * np.sign(Rx3[i,j]) * np.sign(Px3[i,j]))
        _Rx3[i,j] = Rx3[i-k,j]
        l = int(3 * np.sign(Ry3[i,j]) * np.sign(Py3[i,j])) 
        _Ry3[i,j] = Ry3[i,j-l]

for i in range(5, height-5) :
    for j in range(5, width-5):
        k = int(5 * np.sign(Rx5[i,j]) * np.sign(Px5[i,j])) 
        _Rx5[i,j] = Rx5[i-k,j]
        l = int(5 * np.sign(Ry5[i,j]) * np.sign(Py5[i,j])) 
        _Ry5[i,j] = Ry5[i,j-l]

for i in range(7, height-7) :
    for j in range(7, width-7):
        k = int(7 * np.sign(Rx7[i,j]) * np.sign(Px7[i,j])) 
        _Rx7[i,j] = Rx7[i-k,j]
        l = int(7 * np.sign(Ry7[i,j]) * np.sign(Py7[i,j])) 
        _Ry7[i,j] = Ry7[i,j-l]
 
for i in range(9, height-9) :
    for j in range(9, width-9):
        k = int(9 * np.sign(Rx9[i,j]) * np.sign(Px9[i,j])) 
        _Rx9[i,j] = Rx9[i-k,j]
        l = int(9 * np.sign(Ry9[i,j]) * np.sign(Py9[i,j])) 
        _Ry9[i,j] = Ry9[i,j-l]
       
for i in range(11, height-11) :
    for j in range(11, width-11):        
        k = int(11 * np.sign(Rx11[i,j]) * np.sign(Px11[i,j])) 
        _Rx11[i,j] = Rx11[i-k,j]
        l = int(11 * np.sign(Ry11[i,j]) * np.sign(Py11[i,j])) 
        _Ry11[i,j] = Ry11[i,j-l]
   
# print(np.max(_Ry11), np.min(_Ry11))
# 4-----------------------------------------------------------------------
RecF3 = np.zeros((height,width), float)
RecF5 = np.zeros((height,width), float)
RecF7 = np.zeros((height,width), float)
RecF9 = np.zeros((height,width), float)
RecF11 = np.zeros((height,width), float)

for i in range(0, height) :
    for j in range(0, width):        
        if np.fabs(_Rx3[i,j]) < np.fabs(_Ry3[i,j]) :
            RecF3[i,j] = np.fabs(_Ry3[i,j]) * np.sign(Py3[i,j])
        else:
            RecF3[i,j] = np.fabs(_Rx3[i,j]) * np.sign(Px3[i,j]) 
                  
        if np.fabs(_Rx5[i,j]) < np.fabs(_Ry5[i,j]) :
            RecF5[i,j] = np.fabs(_Ry5[i,j])*np.sign(Py5[i,j])
        else:
            RecF5[i,j] = np.fabs(_Rx5[i,j])*np.sign(Px5[i,j])
            
        if np.fabs(_Rx7[i,j]) < np.fabs(_Ry7[i,j]) :
            RecF7[i,j] = np.fabs(_Ry7[i,j])*np.sign(Py7[i,j])
        else:
            RecF7[i,j] = np.fabs(_Rx7[i,j])*np.sign(Px7[i,j])
            
        if np.fabs(_Rx9[i,j]) < np.fabs(_Ry9[i,j]) :
            RecF9[i,j] = np.fabs(_Ry9[i,j])*np.sign(Py9[i,j])
        else:
            RecF9[i,j] = np.fabs(_Rx9[i,j])*np.sign(Px9[i,j])
            
        if np.fabs(_Rx11[i,j]) < np.fabs(_Ry11[i,j]) :
            RecF11[i,j] = np.fabs(_Ry11[i,j])*np.sign(Py11[i,j])
        else:
            RecF11[i,j] = np.fabs(_Rx11[i,j])*np.sign(Px11[i,j])      

imgOut = imgTemp - RecF3 - RecF5- RecF7 - RecF9 - RecF11
filtr = RecF3 + RecF5 + RecF7 + RecF9 + RecF11
#print(np.max(RecF3), np.min(RecF3))
#print(np.max(_Rx3), np.min(_Rx3), np.var(_Rx3), _Rx3[:,:])
#print(np.max(filtr), np.min(filtr))
norm_image = cv2.normalize(imgOut, imgOut, 0, 255, norm_type=cv2.NORM_MINMAX)
norm_image = cv2.normalize(filtr, filtr, 0, 255, norm_type=cv2.NORM_MINMAX)
cv2.imwrite('f:/images/deblunomer.jpg', imgOut)
cv2.imwrite('f:/images/filtrnomer.jpg', filtr )
imgt = np.zeros((height,width), float)
imgt = imgOut - imgIn
cv2.imwrite('f:/images/diffnomer.jpg', imgt )




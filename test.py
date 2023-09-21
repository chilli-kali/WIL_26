# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 14:52:55 2023

@author: kawsa
"""

import cv2

cap=cv2.VideoCapture(0,cv2.CAP_DSHOW) #// if you have second camera you can set first parameter as 1
if not cap.isOpened():
    print("Could not open video device")
    while True: 
        ret,frame= cap.read()
        cv2.imshow("Live",frame)
        cv2.waitKey(1)
    cv2.destroyAllWindows()

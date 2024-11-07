#-- !/usr/bin/env python3
#-- -*- coding: utf-8 -*-
#--
#-- ************************************************************************************************************:
#-- ******************************************* OBSCURE / BLUR FACES *******************************************:
#-- ************************************************************************************************************:
#-- Author:   JBALLARD (JEB)                                                                                    :
#-- Date:     2024.2.18                                                                                         :
#-- Script:   IMAGE.BLUR.FACES.py                                                                               :
#-- Purpose:  A python script that loads images, scans image for faces, blurres faces.                          :
#-- Class:    python -m pip install -U opencv-python                                                            :
#-- Version:  1.0                                                                                               :
#-- ************************************************************************************************************:
#-- ************************************************************************************************************:
#--
#-- ********************************************************:
#-- DEFINE PARAMS, CONSTANTS, CONFIG PATHS, CLASSES, & LIBS :
#-- ********************************************************:
import os
import cv2
#--
#-- DEFINE PATH:
IMGPath = os.path.join("//JBALLARD-9520", "C$", "0_SVN", "4_PERSONAL", "PY.PROC.STORE", "JEB.jpg")
IMGOut  = os.path.join("//JBALLARD-9520", "C$", "0_SVN", "4_PERSONAL", "PY.PROC.STORE", "JEB.v2.jpg")
#--
#-- FUNCTION - OBSCURE FACES:
def OBSCURE_Faces(IMGPath, IMGOut):
    #-- LOAD, SCAN IMAGE, & INITIALIZE FACIAL DETECTION MODEL:
    IMGRead     = cv2.imread(IMGPath)
    FACE_Detect = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    #-- DISCOVER FACES:
    DETECT_Faces = FACE_Detect.detectMultiScale(IMGRead, scaleFactor=1.1, minNeighbors=5)
    #--
    #-- OBSCURE/BLUR ALL DISCOVERED FACES:
    for (fx, fy, fw, fh) in DETECT_Faces:
        #--
        FACE_Reg     = IMGRead[fy:fy+fh, fx:fx+fw]
        BLURRED_Face = cv2.GaussianBlur(FACE_Reg, (101, 101), 35)
        IMGRead[fy:fy+fh, fx:fx+fw] = BLURRED_Face
    #--
    #-- SAVE BLURRED IMAGE AS NEW FILE:
    cv2.imwrite(IMGOut, IMGRead)
    print(f"NOTE - ALL FACES HAVE BEEN OBSCURED/BLURRED, SAVED IMAGE AS {IMGOut}:")
#--
#-- EXAMPLE:
OBSCURE_Faces(IMGPath, IMGOut)
#--
#-- ********************************************************:
#-- END OF PYTHON SCRIPT                                    :
#-- ********************************************************:
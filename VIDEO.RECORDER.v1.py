#--!/usr/bin/env python3
#-- -*- coding: Latin-1 -*-
#--
#-- ************************************************************************************************************:
#-- ********************************************** RECORD SCREEN ***********************************************:
#-- ************************************************************************************************************:
#-- Author:   JBALLARD (JEB)                                                                                    :
#-- Date:     2024.6.27                                                                                         :
#-- Script:   VIDEO.RECORDER.v1.py                                                                              :
#-- Purpose:  A python script that records your screen @ 60FPS with High Rez.                                   :
#-- Class:    python -m pip install opencv-python                                                               :
#-- Class:    python -m pip install numpy                                                                       :
#-- Class:    python -m pip install pyautogui                                                                   :
#-- Class:    python -m pip install cv2                                                                         :
#-- Class:    python3 -m pip install opencv-python                                                              :
#-- Class:    python3 -m pip install numpy                                                                      :
#-- Class:    python3 -m pip install pyautogui                                                                  :
#-- Class:    python3 -m pip install cv2                                                                        :
#-- Version:  1.0                                                                                               :
#-- ************************************************************************************************************:
#-- ************************************************************************************************************:
#--
#-- ********************************************************:
#-- DEFINE PARAMS, CONSTANTS, CONFIG PATHS, IMPORT CLASSES  :
#-- ********************************************************:
import cv2
import numpy as np
import pyautogui
#--
#-- SET SCREEN RESOLUTION:
resolution = (1920, 1080)
#--
#-- SET VIDEO CODEC, FILE NAME, & FPS:
codec    = cv2.VideoWriter_fourcc(*"XVID")
filename = "JEB-SCN.WRITER.avi"
fps      = 60.0
#--
out = cv2.VideoWriter(filename, codec, fps, resolution)
cv2.namedWindow("Live", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Live", 480, 270)
#--
#-- LOOP THROUGH VIDEO FRAME WRITES:
while True:
    img   = pyautogui.screenshot() 
    frame = np.array(img)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    #--
    out.write(frame)
    cv2.imshow("Live", frame)
    key = cv2.waitKey(1)
    #--
    if key == ord("s"):
        break
    elif key == ord("r"):
        continue
#--
#-- RELEASE VIDEO WRITER & DESTROY WIN OBJS:
out.release()
cv2.destroyAllWindows()
#--
#-- ********************************************************:
#-- END OF PYTHON SCRIPT                                    :
#-- ********************************************************:
#--
#-- ************************************************************************************************************:
#-- *********************************************** VIDEO OPTIMIZER ********************************************:
#-- ************************************************************************************************************:
#-- Author:   JBALLARD (JEB)                                                                                    :
#-- Date:     2023.2.18                                                                                         :
#-- Script:   IMAGE.ENHANCEMENT.py                                                                              :
#-- Purpose:  A python script that Optimize Video.                                                              :
#-- Version:  1.0                                                                                               :
#-- ************************************************************************************************************:
#-- ************************************************************************************************************:
#--
#-- ********************************************************:
#-- DEFINE PARAMS, CONSTANTS, CONFIG PATHS, IMPORT CLASSES  :
#-- ********************************************************:
#--PIP INSTALL pillow
from PIL import Image,ImageFilter
from PIL import ImageEnhance
#--
im = Image.open('img.jpg')
#--
#-- CHOOSE ENHANCEMENT FILTER:
en = ImageEnhance.Color(im)
en = ImageEnhance.Contrast(im)
en = ImageEnhance.Brightness(im)
#-- PRINT RESULTS:
en = ImageEnhance.Sharpness(im)
#--
en.enhance(1.5).show("enhanced")
#--
#-- ********************************************************:
#-- END OF PYTHON SCRIPT                                    :
#-- ********************************************************:
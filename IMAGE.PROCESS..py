#--
#-- ************************************************************************************************************:
#-- ************************************************ PROCESS IAMGES ********************************************:
#-- ************************************************************************************************************:
#-- Author:   JBALLARD (JEB)                                                                                    :
#-- Date:     2023.2.18                                                                                         :
#-- Script:   IMAGE.PROCESS.py                                                                                  :
#-- Purpose:  A python script that Process & Optimizes images.                                                  :
#-- Version:  1.0                                                                                               :
#-- ************************************************************************************************************:
#-- ************************************************************************************************************:
#--
#-- *************************************************:
#-- DEFINE PARAMS, CONFIG PATHS, IMPORT CLASSES      :
#-- *************************************************:
#-- INSTALL PILLOW MODULE:
import PIL
#--
#-- CROPE:
im = PIL.Image.open("Image1.jpg")
im = im.crop((34, 23, 100, 100))
#--
#-- RESIZE:
im = PIL.Image.open("Image1.jpg")
im = im.resize((50, 50))
#--
#-- FLIP:
im = PIL.Image.open("Image1.jpg")
im = im.transpose(PIL.Image.FLIP_LEFT_RIGHT)
#--
#-- ROTATE
im = PIL.Image.open("Image1.jpg")
im = im.rotate(360)
#--
#-- COMPRESS:
im = PIL.Image.open("Image1.jpg")
im.save("Image1.jpg", optimize=True, quality=90)
#--
#-- BLUR:
im = PIL.Image.open("Image1.jpg")
im = im.filter(PIL.ImageFilter.BLUR)
#--
#-- SHARPEN:
im = PIL.Image.open("Image1.jpg")
im = im.filter(PIL.ImageFilter.SHARPEN)
#--
#-- SET BRIGHTNESS:
im = PIL.Image.open("Image1.jpg")
im = PIL.ImageEnhance.Brightness(im)
im = im.enhance(1.5)
#--
#-- SET CONTRAST:
im = PIL.Image.open("Image1.jpg")
im = PIL.ImageEnhance.Contrast(im)
im = im.enhance(1.5)
#--
#-- ADD FILTERS:
im = PIL.Image.open("Image1.jpg")
im = PIL.ImageOps.grayscale(im)
im = PIL.ImageOps.invert(im)
im = PIL.ImageOps.posterize(im, 4)
#--
#-- SAVE IMAGE:
im.save("Image1.jpg")
#--
#-- *************************************************:
#-- END OF SCRIPT                                    :
#-- *************************************************:
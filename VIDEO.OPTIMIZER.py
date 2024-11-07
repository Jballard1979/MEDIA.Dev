#--
#-- ************************************************************************************************************:
#-- *********************************************** VIDEO OPTIMIZER ********************************************:
#-- ************************************************************************************************************:
#-- Author:   JBALLARD (JEB)                                                                                    :
#-- Date:     2023.2.18                                                                                         :
#-- Script:   VIDEO.OPTIMIZER.py                                                                                :
#-- Purpose:  A python script that Optimize Video.                                                              :
#-- Class:    python -m pip install moviepy                                                                     :
#-- Version:  1.0                                                                                               :
#-- ************************************************************************************************************:
#-- ************************************************************************************************************:
#--
#-- ********************************************************:
#-- DEFINE PARAMS, CONSTANTS, CONFIG PATHS, IMPORT CLASSES  :
#-- ********************************************************:
import moviepy.editor as pyedit
#--
#-- LOAD VIDEO:
video = pyedit.VideoFileClip("vid.mp4")
#-- TRIM:
vid1 = video.subclip(0, 10)
vid2 = video.subclip(20, 40)
final_vid = pyedit.concatenate_videoclips([vid1, vid2])
#-- SPEED UP VIDEO:
final_vid = final_vid.speedx(2)
#-- ADD AUDIO TO VIDEO:
aud = pyedit.AudioFileClip("bg.mp3")
final_vid = final_vid.set_audio(aud)
#-- REVERSE VIDEO:
final_vid = final_vid.fx(pyedit.vfx.time_mirror)
#-- MERGE 2 VIDEOS:
vid1 = pyedit.VideoFileClip("vid1.mp4")
vid2 = pyedit.VideoFileClip("vid2.mp4")
final_vid = pyedit.concatenate_videoclips([vid1, vid2])
#-- ADD VFX TO VIDEO:
vid1 = final_vid.fx(pyedit.vfx.mirror_x)
vid2 = final_vid.fx(pyedit.vfx.invert_colors)
final_vid = pyedit.concatenate_videoclips([vid1, vid2])
#-- ADD IMAGES TO VIDEO:
img1 = pyedit.ImageClip("img1.jpg")
img2 = pyedit.ImageClip("img2.jpg")
final_vid = pyedit.concatenate_videoclips([img1, img2])
#-- SAVE VIDEO:
final_vid.write_videofile("final.mp4")
#--
#-- ********************************************************:
#-- END OF PYTHON SCRIPT                                    :
#-- ********************************************************:
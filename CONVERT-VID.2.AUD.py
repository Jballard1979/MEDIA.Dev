#--!/usr/bin/env python3
#-- -*- coding: Latin-1 -*-
#--
#-- ************************************************************************************************************:
#-- ********************************************* CONVERT MP4 TO MP3 *******************************************:
#-- ************************************************************************************************************:
#-- Author:   JBALLARD (JEB)                                                                                    :
#-- Date:     2024.4.30                                                                                         :
#-- Script:   CONVERT-VID.2.AUD.py                                                                              :
#-- Purpose:  A python script that converts all MP4 VIDEO files to MP3 AUDIO files.                             :
#-- Class:    python -m pip install moviepy                                                                     :
#-- Class:    python -m pip install AudioFileClip                                                               :
#-- Version:  1.0                                                                                               :
#-- ************************************************************************************************************:
#-- ************************************************************************************************************:
#--
#-- ********************************************************:
#-- DEFINE PARAMS, CONSTANTS, CONFIG PATHS, IMPORT CLASSES  :
#-- ********************************************************:
import os
from moviepy.editor import *
#--
def convert_mp4_to_mp3(mp4_file, mp3_file):
    clip = AudioFileClip(mp4_file)
    clip.write_audiofile(mp3_file)
    clip.close()
#--
#-- SPECIFY MP4 & MP3 DIRS:
MP4Dir = "//JBALLARD-9520/C$/0_SVN/4_PERSONAL/YT-MEDIA"
MP3Dir = "//JBALLARD-9520/C$/0_SVN/4_PERSONAL/YT-MEDIA"
#--
#-- ITERATE THRU ALL FILES IN MP4 DIR:
for file in os.listdir(MP4Dir):
    if file.endswith(".mp4"):
        MP4Path = os.path.join(MP4Dir, file)
        #-- GENERATE CORRESPONDING MP3 FILENAME:
        MP3FName = os.path.splitext(file)[0] + ".mp3"
        MP3Path  = os.path.join(MP3Dir, MP3FName)
        #-- CONVERT MP4 TO MP3:
        convert_mp4_to_mp3(MP4Path, MP3Path)
#--
#-- PROCESS COMPLETED:
print("NOTE - ALL MP4 VIDEO FILES CONVERTED TO MP3 AUDIO FILES:")
#--
#-- ********************************************************:
#-- END OF PYTHON SCRIPT                                    :
#-- ********************************************************:
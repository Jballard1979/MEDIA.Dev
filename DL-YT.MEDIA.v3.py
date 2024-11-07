#-- !/usr/bin/env python3
#-- -*- coding: utf-8 -*-
#--
#-- ************************************************************************************************************:
#-- ******************************************* DOWNLOAD YOUTUBE MEDIA *****************************************:
#-- ************************************************************************************************************:
#-- Author:   JBALLARD (JEB)                                                                                    :
#-- Date:     2024.4.24                                                                                         :
#-- Script:   DL-YT.MEDIA.v3.py                                                                                 :
#-- Purpose:  A python script that Downlaods the specified YouTube Audio & Video files.                         :
#-- Usage:    Copy YouTube URLS into the following file --> "DL-YT.MEDIA.jeb".                                  :
#-- Class:    python -m pip install -U pytubeFix                                                                :
#-- Class:    python -m pip install -U pytube                                                                   :
#-- Class:    python -m pip install -U moviepy                                                                  :
#-- Class:    python -m pip install -U moviepy.editor                                                           :
#-- Version:  3.0                                                                                               :
#-- ************************************************************************************************************:
#-- ************************************************************************************************************:
#--
#-- ********************************************************:
#-- DEFINE PARAMS, CONSTANTS, CONFIG PATHS, CLASSES, & LIBS :
#-- ********************************************************:
import os
import logging
from pytubefix import YouTube
from moviepy.editor import *
#--
#-- CONFIGURE URL & DIR PATHS:
VIDUrl  = 'DL-YT.MEDIA.jeb'
OUTPath = os.path.join("//JBALLARD-9520", "C$", "0_SVN", "4_PERSONAL", "PY.PROC.STORE")
#--
#-- CONFIGURE LOGGING:
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
#--
#-- FUNCTION - MP4 TO MP3 CONVERT:
def MP4_2_MP3_Conv(MP4_File, MP3_File):
    try:
        clip = AudioFileClip(MP4_File)
        clip.write_audiofile(MP3_File)
        clip.close()
    except Exception as e:
        logging.error(f"ERROR - FAILED TO CONVERT {MP4_File} TO MP3: {e}")
#--
#-- VERIFY OUTPath EXISTS:
if not os.path.exists(OUTPath):
    os.makedirs(OUTPath)
#--
#-- LOAD YOUTUBE LIST CONTAINING DESIRED URL's:
try:
    with open(VIDUrl, 'r') as link_file:
        VIDUrls = link_file.readlines()
except FileNotFoundError:
    logging.error(f"ERROR - THE URL - '{VIDUrl}' WAS NOT FOUND:")
    exit(1)
#--
#-- LOOP THRU & DOWNLOAD VIDEO URL's:
for VIDUrl in VIDUrls:
    VIDUrl = VIDUrl.strip()
    if not VIDUrl:
        continue
    try:
        yt = YouTube(VIDUrl)
    except Exception as e:
        logging.error(f"ERROR - FAILED TO CONNECT TO THE URL - '{VIDUrl}': {e}")
        continue
    #--
    #-- RETRIEVE VIDEO CONTAINING HIGHEST RESOLUTION:
    MP4Streams = yt.streams.filter(file_extension='mp4')
    if MP4Streams:
        DLVideo = MP4Streams.get_highest_resolution()
        try:
            DLVideo.download(output_path=OUTPath)
            logging.info(f"NOTE - THE DOWNLOAD PROCESS WAS SUCCESSFUL - '{VIDUrl}'")
        except Exception as e:
            logging.error(f"ERROR - FAILED TO DOWNLOAD URL - '{VIDUrl}': {e}")
#--
logging.info("NOTE - SUCCESSFULLY DOWNLOADED ALL MP4(s):")
#--
#-- CONVERT MP4 TO MP3:
logging.info("PLEASE WAIT...PREPARING TO CONVERT MP4 VIDEOS TO MP3 AUDIO FILES:")
#--
#-- USER ACTION REQUIRED:
CONF = input("HELLO, WOULD YOU LIKE TO CONVERT THE MP4 FILES TO MP3 (y/n)? ")
if CONF.lower() in ['y', 'yes']:
    #--
    #-- ITERATE THRU ALL FILES IN MP4 DIR:
    for file in os.listdir(OUTPath):
        if file.endswith(".mp4"):
            MP4Path  = os.path.join(OUTPath, file)
            MP3Frame = os.path.splitext(file)[0] + ".mp3"
            MP3Path  = os.path.join(OUTPath, MP3Frame)
            MP4_2_MP3_Conv(MP4Path, MP3Path)
    logging.info("NOTE - SUCCESSFULLY GENERATED MP3 FILES:")
else:
    logging.info("NOTE - USER SELECTED TO DECLINE MP4 TO MP3 CONVERSION:")
#--
#-- ********************************************************:
#-- END OF PYTHON SCRIPT                                    :
#-- ********************************************************:
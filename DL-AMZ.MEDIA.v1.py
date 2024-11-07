#-- !/usr/bin/env python3
#-- -*- coding: utf-8 -*-
#--
#-- ************************************************************************************************************:
#-- ******************************************* DOWNLOAD YOUTUBE MEDIA *****************************************:
#-- ************************************************************************************************************:
#-- Author:   JBALLARD (JEB)                                                                                    :
#-- Date:     2024.8.24                                                                                         :
#-- Script:   DL-AMZ.MEDIA.v1.py                                                                                :
#-- Purpose:  A python script that converts Amazon Audible "aax" files to "mp3 files.                           :
#-- Usage:    Copy AMAZON AUDIBLE files to dir --> "//JBALLARD-9520/C$/0_SVN/4_PERSONAL/PY.PROC.STOREDL/".      :
#-- Class:    python -m pip install -U subprocess pyaaudible AudibleBook                                        :
#-- Version:  1.0                                                                                               :
#-- ************************************************************************************************************:
#-- ************************************************************************************************************:
#--
#-- ********************************************************:
#-- DEFINE PARAMS, CONSTANTS, CONFIG PATHS, CLASSES, & LIBS :
#-- ********************************************************:
import os
import sys
import subprocess
from pyaaudible import AudibleBook
#--
#-- CONFIGURE URL & DIR PATHS:
INPPath = 'DL-YT.MEDIA.jeb'
OUTPath = os.path.join("//JBALLARD-9520", "C$", "0_SVN", "4_PERSONAL", "PY.PROC.STORE")
#--
#-- FUNCTION - CONVERT AMAZON AUDIBLE TO MP3:
def convert_aax_to_mp3(input_path, output_path):
    book = AudibleBook()
    try:
        book.open(input_path)
        track_count = len(book)
        #--
        print(f"NOTE - PROCESSING {track_count} AUDIO TRACKS, PLEASE WAIT...")
        for i in range(track_count):
            track = book[i]
            output_filename = os.path.join(output_path, f"{i}.mp3")
            command = ["ffmpeg", "-loglevel", "quiet", "-y", "-i", track.filename(), output_filename]
            subprocess.run(command)
        #--
        print("NOTE - SUCCESSFULLY CONVERTED AUDIO FILE(S):")
    except Exception as e:
        #--
        print(f"FAILURE - AN ERROR OCCURRED DURING CONVERSION PROCESS: {e}")
#--
#-- FUNCTION - MAIN:
if __name__ == "__main__":
    if len(sys.argv) < 3:
        #--
        print("USAGE: python script.py input_folder output_folder")
        sys.exit(1)
    #--
    input_folder = sys.argv[1]
    output_folder = sys.argv[2]
    if not os.path.exists(input_folder):
        #--
        print(f"FAILURE  - INPUT DIRECTORY '{input_folder}' DOES NOT EXIST:")
        sys.exit(1)
    if not os.path.isdir(output_folder):
        os.makedirs(output_folder, exist_ok=True)    
    #--
    #-- LOOP THRU INPUT FOLDER TO PROCESS CONVERSION ROUTINE:
    for root, _, files in os.walk(input_folder):
        for file in files:
            if file.endswith(".aax"):
                convert_aax_to_mp3(os.path.join(root, file), output_folder)
#--
#-- ********************************************************:
#-- END OF PYTHON SCRIPT                                    :
#-- ********************************************************:
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
#-- Class:    python -m pip install -U Audible Books Track                                                      :
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
import Books
import Track

OUTPath = os.path.join("//JBALLARD-9520", "C$", "0_SVN", "4_PERSONAL", "PY.PROC.STORE")

def convert_aax_to_mp3(input_path, output_path):
    book = Book()
    try:
        book.open(input_path)
        track_count = len(book)
        print(f"Processing {track_count} tracks...")
        for i in range(track_count):
            track = book[i]
            output_filename = os.path.join(output_path, f"{i}.mp3")
            command = ["ffmpeg", "-loglevel", "quiet", "-y", "-i", track.filename(), output_filename]
            subprocess.run(command)
        print("Conversion completed.")
    except Exception as e:
        print(f"An error occurred during the conversion process: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python script.py input_folder OUTPath")
        sys.exit(1)

    input_folder = sys.argv[1]
    OUTPath = sys.argv[2]
    if not os.path.exists(input_folder):
        print(f"Input folder '{input_folder}' does not exist.")
        sys.exit(1)

    if not os.path.isdir(OUTPath):
        os.makedirs(OUTPath, exist_ok=True)

    for root, _, files in os.walk(input_folder):
        for file in files:
            if file.endswith(".aax"):
                convert_aax_to_mp3(os.path.join(root, file), OUTPath)
#-- ********************************************************:
#-- END OF PYTHON SCRIPT                                    :
#-- ********************************************************:
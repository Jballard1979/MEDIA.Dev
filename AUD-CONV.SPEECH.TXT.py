#--
#-- ************************************************************************************************************:
#-- ******************************************* SPEECH & TEXT CONVERTER ****************************************:
#-- ************************************************************************************************************:
#-- Author:   JBALLARD (JEB)                                                                                    :
#-- Date:     2024.2.18                                                                                         :
#-- Script:   AUD-CONV.SPEECH.TXT.py                                                                            :
#-- Purpose:  A python script that converts speech to text & text to speech.                                    :
#-- Class:    python -m pip install gTTS                                                                        :
#-- Class:    python -m pip install speechrecognition                                                           :
#-- Class:    python -m pip install pyaudio                                                                     :
#-- Class:    python -m pip install LooseVersion                                                                :
#-- Version:  1.0                                                                                               :
#-- ************************************************************************************************************:
#-- ************************************************************************************************************:
#--
#-- ********************************************************:
#-- DEFINE PARAMS, CONSTANTS, CONFIG PATHS, IMPORT CLASSES  :
#-- ********************************************************:
from gtts import gTTS
import os
import speech_recognition as sr
#--
#-- CONVERTS INPUT TEXT TO SPEECH:
def text_to_speech():
    text = input("ENTER DESIRED TEXT:- ")
    tts = gTTS(text)
    tts.save("OUTPUT.mp3")
    os.system("START OUTPUT.mp3")
#--
#-- CONVERTS SPEECH TO TEXT VIA MICROPHONE:
def speech_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("SPEAK DESIRED TEXT...")
        recognizer.adjust_for_ambient_noise(source, duration=0.2)
        audio = recognizer.listen(source)
    try:
        print("PLEASE WAIT... RECOGNIZING...")
        text = recognizer.recognize_google(audio)
        print(f"YOU'VE SPOKEN: {text}")
    except sr.UnknownValueError:
        print("ERROR - FAILED TO UNDERSTAND AUDIO:")
    except sr.RequestError as e:
        print(f"ERROR: {e}")
#--
#-- MENU DRIVEN INTERFACE WITH OPTIONS:
while True:
    print("PLEASE SELECT A MENU OPTION:")
    print("1. TEXT TO SPEECH:")
    print("2. SPEECH TO TEXT:")
    print("3. EXIT:")
    #--
    choice = input("CHOICE (1/2/3): ")
    if choice == '1':
        text_to_speech()
    elif choice == '2':
        speech_to_text()
    elif choice == '3':
        print("EXITING PROGRAM...")
        break
    else:
        print("ERROR - INVALID CHOICE, PLEASE SELECT A VALID MENU OPTION:")
#--
#-- ********************************************************:
#-- END OF PYTHON SCRIPT                                    :
#-- ********************************************************:
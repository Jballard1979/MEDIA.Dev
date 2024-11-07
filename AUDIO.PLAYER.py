#--
#-- ************************************************************************************************************:
#-- ************************************************ MUSIC PLAYER **********************************************:
#-- ************************************************************************************************************:
#-- Author:   JBALLARD (JEB)                                                                                    :
#-- Date:     2023.2.18                                                                                         :
#-- Script:   AUDIO.PLAYER.py                                                                                   :
#-- Purpose:  A python script that plays audio files.                                                           :
#-- Class:    python -m pip install pygame                                                                      :
#-- Class:    python -m pip install moviepy                                                                     :
#-- Version:  1.0                                                                                               :
#-- ************************************************************************************************************:
#-- ************************************************************************************************************:
#--
#-- ********************************************************:
#-- DEFINE PARAMS, CONSTANTS, CONFIG PATHS, IMPORT CLASSES  :
#-- ********************************************************:
import tkinter as tk
import os
from pygame import mixer
#--
class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Music Player")
        self.root.geometry("300x100")
        #-- INITIALIZE PYGAME MIXER:
        mixer.init()
        #-- GENERATE VARS TO STORE CURRENT PLAY STATUS:
        self.playing = False
        # GENERATE VAR TO STORE CURRENTLY SELECTED AUDIO FILE:
        self.current_song = None
        #-- GENERATE UI ELEMENTS:
        self.label = tk.Label(root, text="Music Player")
        self.label.pack()
        self.play_button = tk.Button(root, text="Play", command=self.play_music)
        self.play_button.pack()
        self.stop_button = tk.Button(root, text="Stop", command=self.stop_music)
        self.stop_button.pack()
        self.browse_button = tk.Button(root, text="Browse", command=self.browse_music)
        self.browse_button.pack()
    def play_music(self):
        if self.current_song:
            if not self.playing:
                mixer.music.load(self.current_song)
                mixer.music.play()
                self.play_button.config(text="Pause")
                self.playing = True
            else:
                mixer.music.pause()
                self.play_button.config(text="Play")
                self.playing = False
    def stop_music(self):
        mixer.music.stop()
        self.play_button.config(text="Play")
        self.playing = False
    def browse_music(self):
        self.current_song = tk.filedialog.askopenfilename(initialdir=os.getcwd(), title="Select Song",
            filetypes=(("Audio Files", "*.mp3"), ("All Files", "*.*")))
        self.label.config(text=os.path.basename(self.current_song))
if __name__ == '__main__':
    root = tk.Tk()
    music_player = MusicPlayer(root)
    root.mainloop()
#--
#-- ********************************************************:
#-- END OF PYTHON SCRIPT                                    :
#-- ********************************************************:
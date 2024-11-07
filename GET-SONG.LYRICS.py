#--
#-- ************************************************************************************************************:
#-- ********************************************** LYRIC RETRIEVER *********************************************:
#-- ************************************************************************************************************:
#-- Author:   JBALLARD (JEB)                                                                                    :
#-- Date:     2023.2.18                                                                                         :
#-- Script:   GET-SONG.LYRICS.py                                                                                :
#-- Purpose:  A python script retrieves lyrics of any desired song.                                             :
#-- Class:    python -m pip install lyricsgenius                                                                :
#-- Version:  1.0                                                                                               :
#-- ************************************************************************************************************:
#-- ************************************************************************************************************:
#--
#-- ********************************************************:
#-- DEFINE PARAMS, CONSTANTS, CONFIG PATHS, IMPORT CLASSES  :
#-- ********************************************************:
import lyricsgenius
#--
def get_song_lyrics(api_key, artist_name, song_title):
    genius = lyricsgenius.Genius(api_key)
    artist = genius.search_artist(artist_name, max_songs=5, sort="title")
    song = artist.song(song_title)
    return song.lyrics
#--
if __name__ == "__main__":
    #-- ENTER YOUR API KEY:
    api_key = "xxxxxxxxxxxxxxxxxxxxx"
    #--
    #-- PROVIDE ARTIST NAME & SONG TITLE:
    artist_name = "TOOL"
    song_title = "46 & 2"
    #--
    lyrics = get_song_lyrics(api_key, artist_name, song_title)
    print(lyrics)
#--
#-- ********************************************************:
#-- END OF PYTHON SCRIPT                                    :
#-- ********************************************************:
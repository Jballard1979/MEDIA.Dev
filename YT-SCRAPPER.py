#-- !/usr/bin/env python3
#-- -*- coding: utf-8 -*-
#--
#-- ************************************************************************************************************:
#-- ********************************************** YOUTUBE SCRAPPER ********************************************:
#-- ************************************************************************************************************:
#-- Author:   JBALLARD (JEB)                                                                                    :
#-- Date:     2024.4.24                                                                                         :
#-- Script:   YT-SCRAPPER.py                                                                                    :
#-- Purpose:  A python script that Scrapes YouTube for desired topics.                                          :
#-- Class:    python -m pip install hugchat                                                                     :
#-- Class:    python -m pip install pytube                                                                      :
#-- Class:    python -m pip install Login                                                                       :
#-- Web:      https://levelup.gitconnected.com/how-to-scrape-youtube-data-for-free-727b78fdd0d8                 :
#-- Version:  3.0                                                                                               :
#-- ************************************************************************************************************:
#-- ************************************************************************************************************:
#--
#-- ********************************************************:
#-- DEFINE PARAMS, CONSTANTS, CONFIG PATHS, CLASSES, & LIBS :
#-- ********************************************************:
import os
import re
from hugchat import hugchat
from hugchat.login import Login
#--
#-- FUNCTION - MP4 TO MP3 CONVERT:
def youtube_links_prompt(field, n_links):
    #--
    #-- LOG IN & GRANT AUTH TO HUGGINGCHAT:
    EMAIL      = "<your_huggingface_email>"
    PASSWD     = "<your_huggingface_password>"
    COOKIEPath = "./cookies/"
    SIGN       = Login(EMAIL, PASSWD)
    COOKIES    = sign.login(cookie_dir_path=COOKIEPath, save_cookies=True)
    CHATBOT    = hugchat.ChatBot(COOKIES=cookies.get_dict())
    #--
    #-- INPUT QUERY:
    input_query = (
        f"GIVE ME THE {n_links} BEST YOUTUBE CHANNEL"
        f" LINKS ABOUT {field}")
    #--
    #-- RETRIEVE RESULTS OF DESIRED PROMPT:
    REZ = chatbot.chat(input_query, web_search=True)
    #-- DEFINE REGULAR EXPRESSION PATTERN FOR URLS:
    URLPattern = r'https?://\S+'
    #--
    #-- DISCOVER URLS:
    YTURLs  = re.findall(URLPattern, str(REZ))
    NEWURLs = []
    for url in YTURLs:
        if '](' in url:
            NEWURL = url.split(']')[0]
            NEWURLs.append(NEWURL)
        else:
            NEWURLs.append(url)
    #-- RETURN URLS:
    return NEWURLs
#--
#-- ********************************************************:
#-- END OF PYTHON SCRIPT                                    :
#-- ********************************************************:
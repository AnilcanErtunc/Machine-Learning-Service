# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 18:47:19 2020

@author: anilc
"""

import os
yol = os.path.dirname(os.path.realpath(__file__)) # dosya yolu bulma kodu

from moviepy.editor import VideoFileClip
video = VideoFileClip(os.path.join(yol,yol,"movie.mp4")) #"path","to"
video.audio.write_audiofile(os.path.join(yol,yol,"movie_sound.mp3"))

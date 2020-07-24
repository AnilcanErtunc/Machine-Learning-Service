 #-*- coding: utf-8 -*-
"""
Created on Mon Jun 22 12:19:03 2020

@author: anilc
"""

import speech_recognition as sr
sr.Microphone(device_index=1)

r=sr.Recognizer()

r.energy_threshold=5000

with sr.Microphone() as source:
        print("Dinleme Aktif")
        audio=r.listen(source)
try:
        text=r.recognize_google(audio,language="tr-TR")                
        print("You said: "+format(text))

except:
        print("Cant recognized")

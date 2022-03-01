# Jeppe Skovby Bjørn
#
# Created using python version 3.9.9
# Packages needed: pyadio & SpeechRecognition
# https://www.thepythoncode.com/article/using-speech-recognition-to-convert-speech-to-text-python

import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    # read the audio data from the default microphone
    audio_data = r.record(source, duration=5)
    print("Recognizing...")
    # convert speech to text
    text = r.recognize_google(audio_data, language="da-DK") # Danish
    #text = r.recognize_google(audio_data) # English
    print(text)
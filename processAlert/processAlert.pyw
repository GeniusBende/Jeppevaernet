#!/usr/bin/python
# Python 3.9.9
# Jeppe Skovby Bjørn
# https://thispointer.com/python-check-if-a-process-is-running-by-name-and-find-its-process-id-pid/

import psutil
import time
import pystray
import threading
import pyautogui

from tkinter import *
from datetime import datetime
from pystray import MenuItem as item
from PIL import Image


_PROCESS_NAME = "Plex Media Server"
_IMAGE = Image.open("assets/icon.png")
_SPY = False
_CHECKDELAY = 1
_MY_THREAD = None

'''
Check if there is any running process that contains the given name processName.
'''
def checkIfProcessRunning(processName):
    #Iterate over the all the running process
    for proc in psutil.process_iter():
        try:
            # Check if process name contains the given name string.
            if processName.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False

def setProcessName(desiredProcessName):
    global _PROCESS_NAME
    _PROCESS_NAME = desiredProcessName

def getDayAndTime():
    # Time now
    now = datetime.now()

    # Sets date formate: dd/mm/YY H:M:S
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

    return dt_string


def setTime():
    global _CHECKDELAY

    while True:
        userInput = pyautogui.prompt('Please insert the amount of delay in seconds')

        if userInput is None:
            break
        
        try:
            _CHECKDELAY = int(userInput)
            break
        except ValueError:
            pyautogui.alert('Input was not a valid number', "Dumbass")

def alert(value):
    if value:
        print(_PROCESS_NAME + " is running | " + getDayAndTime())
    else:
        print(_PROCESS_NAME + " is not running | " + getDayAndTime())

def mainLoop():
    while _SPY:
        value = checkIfProcessRunning(_PROCESS_NAME)

        alert(value)

        time.sleep(_CHECKDELAY)

def stop():
    global _SPY
    _SPY = False

def start():
    global _SPY, _MY_THREAD
    _SPY = True

    if (_MY_THREAD.is_alive()):
        pass
    else:
        _MY_THREAD = threading.Thread(target=mainLoop)
        _MY_THREAD.daemon = True
        _MY_THREAD.start()

def quit():
    global _SPY
    _SPY = False

    programSysTray.stop()
    
menu = (item('Start', start), item('Stop', stop), item('Set delay', setTime), item('Quit', quit))

programSysTray = pystray.Icon("name", _IMAGE, "Spying", menu)
programSysTray.run()

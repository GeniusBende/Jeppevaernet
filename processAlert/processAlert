# Python 3.9.9
# Jeppe Skovby Bjørn
# https://thispointer.com/python-check-if-a-process-is-running-by-name-and-find-its-process-id-pid/

import psutil
import time
from datetime import datetime

_PROCESS_NAME = "chrome"

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

if __name__ == "__main__":
    while True:
        myVar = checkIfProcessRunning(_PROCESS_NAME)

        if myVar:
            print(_PROCESS_NAME + " is running | " + getDayAndTime())
        else:
            print(_PROCESS_NAME + " is not running | " + getDayAndTime())

        time.sleep(1)

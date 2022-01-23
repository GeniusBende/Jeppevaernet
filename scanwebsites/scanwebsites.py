# Python 3.10.0

import site
import requests
import time
import smtplib
from email.message import EmailMessage
import hashlib
from urllib.request import urlopen
import os.path

def send_email():
    msg = EmailMessage()
    msg.set_content(url)
    msg['From'] = 'ScannerDinHjemmeside@gmail.com'
    msg['To'] = 'stefan.thuesen@gmail.com'
    msg['Subject'] = 'New Daily Activity Report'
    fromaddr = 'ScannerDinHjemmeside@gmail.com'
    toaddrs = ['stefan.thuesen@gmail.com']
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login('ScannerDinHjemmeside@gmail.com', 'PASSWORD HERE!')
    server.send_message(msg)
    server.quit()

url = 'https://9gag.com/'

'''
if os.path.isfile(".\currenthash.txt"):
    response = urlopen(url).read()
    newHash = hashlib.sha224(response).hexdigest()
    print(newHash)
    currentHash = open("currenthash.txt", "w+")
    if newHash != currentHash.read():
        currentHash.write(newHash)
        currentHash.close
        send_email()
    else:
        currentHash.close
else:
    response = urlopen(url).read()
    currentHash = open("currenthash.txt", "w")
    currentHash.write(hashlib.sha224(response).hexdigest())
    currentHash.close
'''

urls = []
tags = []
data = []
sites = open("sites.txt", "r")
if os.path.isfile("sites.txt"):
    for line in sites:
        data.append(line.strip())
        line = line.strip()
        splitline = line.split(";")
        tags.append(splitline[0])
        urls.append(splitline[1])
else:
    exit()
print(data)
x = data.index("enghaven;https://findbolig.nu/LandingPages/enghaven")
print (x)

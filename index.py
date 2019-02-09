#!/usr/bin/python3
# -*- coding: utf-8 -*
#
# By TheDoudou
#

import cgi, subprocess, pyautogui, sys, time

form = cgi.FieldStorage()


print("Content-type: text/html; charset=utf-8\n")

if form.getvalue("code") != '1':
    print("""Mauvais mot de passe<br><br>""")
    print("""<img src="img.py" alt="screenshot">""")
    
    sys.exit()

def getClipboardData():
    p = subprocess.Popen(['xclip','-sel', '-c', '-o'], stdout=subprocess.PIPE)
    retcode = p.wait()
    data = p.stdout.read()
    return data

def cleanClipboardData():
    subprocess.Popen(['echo', '-n', '|', 'xclip', '-selection', 'clipboard'], stdout=subprocess.PIPE)
    return 1



if form.getvalue("clic") == '1':
    pyautogui.hotkey('ctrl', 'multiply') # Get LS Link clipboard
    time.sleep(2)


if form.getvalue("clic") == '2':
    pyautogui.hotkey('shift', 'w') # Stop Server
    cleanClipboardData()
    time.sleep(1)
    pyautogui.hotkey('shift', 'q') # Start Server
    time.sleep(3)
    pyautogui.hotkey('ctrl', 'multiply')
    time.sleep(1)

clip = getClipboardData() # Get Clipboard 

print("""<!DOCTYPE html>
<html>
<head>
    <title>Auto Liveshare</title>
</head>
<body><a target="_blank" href=\"""")
print(clip.decode('utf-8'))
print("""\">""")
print(clip.decode('utf-8'))
print("""</a>""")
print("""<br><br>
[<a href="index.py?code=42">REFRESH</a>] (use this for reaload page)<br><br>
[<a href="?clic=1&code=42">Get Copy Link</a>] - """)
print("""[<a href="?clic=2&code=42">Restart Live Share Server</a>]""")
print("""<br><br>(live view)<br>""")

print("""<img src="img.py" alt="screenshot">""")

print("""</a></body>
</html>
""")


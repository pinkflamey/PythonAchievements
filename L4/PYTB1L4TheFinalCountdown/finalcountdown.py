import time
from art import *
from sys import platform
from time import sleep
from os import system
import webbrowser

if platform == "win32":
    system("mode con: cols=80 lines=15")
else:
    system("resize -s 15 80")

def clearScreen(): # Clears the screen for Windows, Mac and Linux
    if platform == "win32":
        system('cls')
    else:
        system('clear')

count = 1000
counting = True

for n in range(count):
    printable = text2art(str(count), font="block")
    print(printable)
    count -= 1
    time.sleep(1)
    clearScreen()
    
if platform == "win32":
    system("mode con: cols=47 lines=8")
else:
    system("resize -s 8 47")

print(text2art("Take off!"))

sleep(1)

webbrowser.open_new_tab("https://youtu.be/ViNcBQ8cDA0?t=31")
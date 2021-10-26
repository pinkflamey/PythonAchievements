from os import system
from sys import platform

platform = platform
def clearScreen(): # Clears the screen for Windows, Mac and Linux
    if platform == "win32":
        system('cls')
    else:
        system('clear')
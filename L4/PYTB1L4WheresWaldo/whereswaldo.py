import os
import random
from sys import platform
from time import sleep

def clearScreen(): # Clears the screen for Windows, Mac and Linux
    if platform == "win32":
        os.system('cls')
    else:
        os.system('clear')


people = ["Waldo","Jackson","Ray","Eric","Vaughn","Jesse","Herbert","Robert", "Rodrigo","Elija","Sasha","Nathaniel","Ellie","Allison","Jeremiah", "Paula", "Alisha","Tory","Troy", "Faye"]

print(", ".join(people)) # Prints all the people unshuffled, with ", " in between to make it ~fancy~

random.shuffle(people)


missing = input("Search for person with the name: ").capitalize() # Makes sure the missing name's first letter is capitalized

print("Okay! I'll look for " + missing + "!")

sleep(2)
clearScreen()

found = False

for name in people: # For all people in the list,
    if name == missing: # If the name is the same as the missing name:
        print("Found you, " + missing + "!")
        found = True # Tells the script the missing person is found
        break # Exit the for loop
    print(name) # If the person was not missing, print their name and continue
    sleep(1)

if found == False: # If the missing person was not found:s
    print("I couldn't find " + missing + "...")

input("\n\nPress enter to quit...")
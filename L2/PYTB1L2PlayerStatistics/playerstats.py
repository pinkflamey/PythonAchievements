import os
from sys import platform

# Statistic variables
currenthealth = 0.0
strength = 0
intelligence = 0
charisma = 0
alive = False
speed = 0
gender = ""
pronouns = ""
wisdom = 0
money = 0.0

# Function that loads the statistics of the selected character
def loadStats(character):
    # Make statistic variables global, so that the changes to them made inside the function will be stored outside of the function
    global currenthealth
    global strength
    global intelligence
    global charisma
    global alive
    global speed
    global gender
    global pronouns
    global wisdom
    global money
    if character == "Aether":
        currenthealth = 15.5
        strength = 13
        intelligence = 18
        charisma = 10
        alive = True
        speed = 19
        gender = "Non-binary"
        pronouns = "he/him" + " " + "they/them"
        wisdom = 7
        money = 0.5
    if character == "Joe":
        currenthealth = 6.0
        strength = 5
        intelligence = 10
        charisma = 12
        alive = True
        speed = 10
        gender = "Male"
        pronouns = "he/him"
        wisdom = 7
        money = 10.0
    if character == "Karen":
        currenthealth = 20.0
        strength = 5
        intelligence = 4
        charisma = 4
        alive = True
        speed = 14
        gender = "Female"
        pronouns = "she/her"
        wisdom = 1
        money = 100.0
    if character == "Aiden":
        currenthealth = 20.0
        strength = 20
        intelligence = 12
        charisma = 18
        alive = True
        speed = 14
        gender = "Agender"
        pronouns = "they/them"
        wisdom = 13
        money = 5.0

def clearScreen(): # Clears the screen for Windows, Mac and Linux
    if platform == "win32":
        os.system('cls')
    else:
        os.system('clear')

# charactersList is for display purposes; charRawList is for checking if the input is valid
charactersList = [" ", "1. Aether", "2. Joe", "3. Karen", "4. Aiden"]
charRawList = ["Aether", "Joe", "Karen", "Aiden"]

# "Movie script" (Displaying what the user will see)
title = "Character viewer".center(50)
menuline = "========================================".center(50)

clearScreen()
print(menuline)
print(title)
print(menuline + "\n")

print(*charactersList, sep="\n".center(40))

charselect = input("\n\nEnter character name: ")

loadStats(charselect)

clearScreen()

# Check if the character input is a valid character; if so, display the stats. If not, display an error
if charselect in charRawList:
    charnametitle = "CHARACTER NAME: " + charselect
    print(menuline)
    print(charnametitle.center(50))
    print(menuline + "\n")

    print("Alive: " + str(alive))
    print("Current health: " + str(currenthealth) + "/20")
    print("Money in pocket: " + str(money) + "G")
    print("Gender: " + gender)
    print("Pronouns: " + pronouns)
    print("Strength: " + str(strength) + "/20")
    print("Intelligence: " + str(intelligence) + "/20")
    print("Wisdom: " + str(wisdom) + "/20")
    print("Charisma: " + str(charisma) + "/20")
    print("Speed: " + str(speed) + "/20")
else:
    print("That is not a valid character.")

# Restarts the script
input("\n\nPress enter to restart...")
clearScreen()
os.system('playerstats.py')
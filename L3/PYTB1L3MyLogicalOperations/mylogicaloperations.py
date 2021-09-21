from sys import platform
from os import system

def clearScreen(): # Clears the screen for Windows, Mac and Linux
    if platform == "win32":
        system('cls')
    else:
        system('clear')

clearScreen()

name = "erwin henraat"
job = "teacher"
moneyInAccount = 1300

#Vervang de ** met de logische operatoren 'and' en/of 'or'

#Zorg dat de if statement de functie buyABrandNewMotorcycle uitvoert als:
# Mijn naam erwin henraat is en ik een baan heb.
# Of als ik meer dan 10000 euro op mijn rekening heb staan.

def buyABrandNewMotorcycle():
    print(":)")

if name == "erwin henraat" and job != None or moneyInAccount > 10000:
    buyABrandNewMotorcycle()


#Maak nu voor jezelf ook een logische voorwaarde waarin je de operatoren 'and' en 'or' gebruikt.

# Mijn take:

hungry = True
bellyfull = True
food = "pepernoten"

if hungry == True and bellyfull == False or food == "pepernoten":
    print("*eats " + food + "*")

# Ik eet wanneer:
# - Ik trek heb (hungry = true) en mijn buik leeg is (bellyfull = false)
# - Het eten pepernoten is
from clearScreen import *
from time import sleep




def makeList():

    newlist = input("Enter groceries for the list, seperated by ', ': ").split(", ")

    for i in range(len(newlist)):
        newlist[i] = newlist[i].lower()

    return newlist

def game():

    groceryList = makeList()

    t = 0

    while True:

        t = input("How much time do you want to remember it?\nTime (seconds): ")
        try:
            t = int(t)
            break
        except ValueError:
            print("\n=== Please enter a full number! ===")

    clearScreen()

    print("You have "+str(t)+" seconds to remember this list!")

    sleep(1)

    print("This is your grocery list:")
    for item in groceryList:
        print("- " + str(item))

    sleep(t)
    clearScreen()

    print("Off to the supermarket!")
    sleep(2)
    clearScreen()

    correct = 0
    mistakecount = 0

    print("There are " + str(len(groceryList)) + " items on your grocery list. Can you name them all?")
    while True:

        x = input("Grab something from the list: ").lower()
        if x in groceryList:

            print("Correct!")
            correct+=1
            print("Correct guesses: " + str(correct))
            if correct == len(groceryList):
                break

        else:

            print("Incorrect!")
            mistakecount+=1
            print("Incorrect guesses: " + str(mistakecount))

    clearScreen()

    print("You remembered all " + str(len(groceryList)) + " groceries! Good job! You made " + str(mistakecount) + " mistakes.")
    sleep(2)

    x = input("Wanna play again? (yes/no): ")
    if x.lower() == "yes":

        clearScreen()
        game()

    else:

        print("Goodbye! (Press [ENTER] to quit)")
        input()

game()
import random

gameRunning = True

words = ["test", "hallo"]

word = random.choice(words)
wordlen = len(word)

splitword = {}
worddisplay = ""


i = 0
while i < wordlen:
    splitword[word[i]] = i

    worddisplay += "|" + str(i)

    i+= 1
worddisplay += "|"


print(splitword)
print(worddisplay)

l = ""

while gameRunning:

    while len(l) != 1:
        l = input("letter: ")

        if len(l) != 1:
            print("Please only input 1 letter!")
    print("letter length is 1")

    if l in splitword.keys(): # If the letter exists as a key
        print("this letter IS in the word")
        


        

    else:
        print("this letter is NOT in the word")
        l = ""




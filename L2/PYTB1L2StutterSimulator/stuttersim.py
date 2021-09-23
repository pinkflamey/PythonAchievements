from random import randint


string = input("Insert string: ")

strlist = string.split()

for word in strlist:
    ran1 = randint(1, 4)
    
    stutword1 = word[0:ran1] 
    
    if stutword1 != word:
        print(stutword1[0:1] + "... " + stutword1 + "... " + word, end=" ")
    else:
        print (word, end=" ")

input("\n\nPress enter to quit...")
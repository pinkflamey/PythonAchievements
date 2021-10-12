


def string_eater(string):
    new_length = len(string) - 1
    string_new = string[0:new_length]
    if len(string_new) == 0:
        print("All your letters are mine!")
    else:
        print(string_new)
        string_eater(string_new)
        


string_eater("Dit is een test string.")
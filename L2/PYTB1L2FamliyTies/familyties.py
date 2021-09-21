

firstname = "Mavis"
surname = "de Ridder"

age = 17

town = "Sassenheim"
address = "Julianalaan 23"

school = "Mediacollege Amsterdam"
school_town = "Amsterdam"
school_address = "Contactweg 36"
distance_to_school = 35.4

hair_colour = ["zwart", "blond"]

print("Ik heet " + firstname + " " + surname + ".", end=" ")
print("Ik ben " + str(age) + " jaar oud, en ik woon in " + town + ". Mijn adres is " + address + ". Mijn haarkleur is nu", end=" ")
print(*hair_colour, sep=" & ", end="")
print(".")
print("Ik ga naar het " + school + " in " + school_town + ". Het adres is " + school_address + ", en de afstand naar school is " + str(distance_to_school) + ".")

input("Press enter to quit...")
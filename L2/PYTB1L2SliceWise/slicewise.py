

tekst = 'De Python lessen worden gegeven voor Erik, Erwin en ook door Hidde'
voornamen = [tekst[37:41], tekst[43:48], tekst[61:67]]
print(*voornamen, sep=" + ")

tekst = "SD vakken zijn bijvoorbeeld Python, UXD, Frontend development en Backend development. Wat leuk!"
vakken = [tekst[0:2], tekst[28:34], tekst[36:39], tekst[41:61], tekst[65:84]]
print(*vakken, sep=" + ")

tekst = "Wat is hier het laatste woord?"
laatste_woord = [tekst[24:29]]
print(*laatste_woord, sep=" + ")

tekst = "Het www is ontwikkeld vanaf 1989 door Tim Berners-Lee"
chars = [tekst[5:9], tekst[29:34]]
print(*chars, sep=" + ")

input("\n\nPress enter to quit...")
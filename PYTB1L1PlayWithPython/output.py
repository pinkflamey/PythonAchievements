Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 2+2
4
>>> 3*10
30
>>> 100-10
90
>>> 25/5
5.0
>>> 10/3
3.3333333333333335
>>> 10//3
3
>>> print('Mijn naam is Mavis')
Mijn naam is Mavis
>>> naam = 'Mavis'
>>> print(naam)
Mavis
>>> print(naam.upper())
MAVIS
>>> print(naam[0:2])
Ma
>>> print(naam[::-1])
sivaM
>>> leeftijd = 17
>>> print('Hallo ' + naam + 'ben je al ' + str(leeftijd) + ' jaar?')
Hallo Mavisben je al 17 jaar?
>>> print('Hallo ' + naam + ' ben je al ' + str(leeftijd) + ' jaar?')
Hallo Mavis ben je al 17 jaar?
>>> leeftijd = leeftijd + 1
>>> leeftijd
18
>>> leeftijd -=1
>>> leeftijd
17
>>> if leeftijd < 18:
	hoelang_tot18jaar = 18 - leeftijd
	print('Over ' + str(hoelang_tot18jaar) + ' jaar wordt je 18')
    elif leeftijd > 18:
	    
SyntaxError: unindent does not match any outer indentation level
>>> if leeftijd < 18:
	hoelang_tot18jaar = 18 - leeftijd
	print('Over ' + str(hoelang_tot18jaar) + ' jaar wordt je 18')
	elif > 18:
		
SyntaxError: invalid syntax
>>> if leeftijd < 18:
	hoelang_tot18jaar = 18 - leeftijd
	print('Over ' + str(hoelang_tot18jaar) + ' jaar wordt je 18')
elif leeftijd > 18:
	hoelang_al18jaar = leeftijd - 18
	print('Het is alweer ' + str(hoelang_al18jaar) + ' jaar geleden dat je 18 werd ;-)')
else:
	print('Je bent precies ' + str(leeftijd) + ' jaar')

	
Over 1 jaar wordt je 18
>>> from random import randint
>>> randint(0,1000)
797
>>> willekeurig_getal = randint(0,1000)
>>> willekeurig_getal
629
>>> willekeurig_getal
629
>>> print('Willekeurig getal tussen 0 en 1000: ' + str(willekeurig getal))
SyntaxError: invalid syntax
>>> print('Willekeurig getal tussen 0 en 1000: ' + str(willekeurig_getal))
Willekeurig getal tussen 0 en 1000: 629
>>> from datetime import datetime
>>> datum = datetime.now()
>>> print(datum)
2021-09-16 08:33:30.498050
>>> datum.strftime('%A %d %B %Y')
'Thursday 16 September 2021'
>>> import locale
>>> locale.setlocale(locale.LC_TIME, 'nl_NL')
'nl_NL'
>>> datum.strftime('%A %d %B %Y')
'donderdag 16 september 2021'
>>> locale.setlocale(locale.LC_TIME, 'it_IT')
'it_IT'
>>> datum.strftime('%A %d %B %Y')
'giovedì 16 settembre 2021'
>>> 
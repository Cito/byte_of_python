#!/usr/bin/python

def potenzsumme(potenz, *parameter):
	'''Gibt die Summe der angegebenen Potzen aller Parameter zurueck.'''
	summe = 0
	for i in parameter:
		summe += pow(i, potenz)
	return summe

print potenzsumme(2, 3, 4) # 3^2 + 4^2
print potenzsumme(2, 10) # 10^2

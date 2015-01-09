#!/usr/bin/python

def printMax(a, b):
	if a > b:
		print a, 'ist Maximalwert'
	else:
		print b, 'ist Maximalwert'

printMax(3, 4) # uebergebe Zahlen direkt als Literale

x = 5
y = 7

printMax(x, y) # uebergebe Variablen als Argumente

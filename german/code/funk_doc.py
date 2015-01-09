#!/usr/bin/python

def printMax(x, y):
	"""Gib das Maximum von zwei Zahlen aus.

	Die beiden Werte muessen ganze Zahlen sein."""
	x = int(x) # Umwandlung in ganze Zahlen, falls moeglich
	y = int(y)

	if x > y:
		print x, 'ist das Maximum'
	else:
		print y, 'ist das Maximum'

printMax(3, 5)
print printMax.__doc__

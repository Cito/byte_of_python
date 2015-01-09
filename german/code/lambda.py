#!/usr/bin/python

def erzeuge_wiederholer(n):
	return lambda s: s * n

verdoppler = erzeuge_wiederholer(2)

print verdoppler('wort')
print verdoppler(5)

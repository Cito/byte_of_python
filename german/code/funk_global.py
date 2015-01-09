#!/usr/bin/python

def funk():
	global x

	print 'x ist', x
	x = 2
	print 'Globales x ist jetzt', x

x = 50
funk()
print 'Der Wert von x ist', x

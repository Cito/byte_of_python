#!/usr/bin/python

def funk(x):
	print 'x ist', x
	x = 2
	print 'Lokales x ist jetzt', x

x = 50
funk(x)
print 'x ist immer noch', x

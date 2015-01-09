#!/usr/bin/python

def funk(a, b=5, c=10):
	print 'a ist', a, 'und b ist', b, 'und c ist', c

funk(3, 7)
funk(25, c=24)
funk(c=50, a=100)

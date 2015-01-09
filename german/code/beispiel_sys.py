#!/usr/bin/python

import sys

print 'Die Kommandozeilenparameter sind:'
for i in sys.argv:
	print i

print '\n\nDer PYTHONPATH ist', sys.path, '\n'

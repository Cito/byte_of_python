#!/usr/bin/python

import sys

try:
	s = raw_input('Geben Sie etwas ein --> ')
except EOFError:
	print '\nWarum haben Sie die Eingabe abgebrochen?'
	sys.exit() # beendet das Programm
except:
	print '\nIrgendein Fehler hat eine Ausnahme ausgeloest.'
	# an dieser Stelle beenden wir das Programm nicht

print 'Fertig'

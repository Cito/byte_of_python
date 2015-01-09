#!/usr/bin/python

while True:
	s = raw_input('Geben Sie etwas ein : ')
	if s == 'ende':
		break
	if len(s) < 3:
		continue
	print 'Die Laenge der Eingabe ist ausreichend.'
	# Verarbeite die Eingabe hier irgendwie...

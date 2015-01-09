#!/usr/bin/python

import time

try:
	f = file('gedicht.txt')
	while True: # unsere uebliche Weise, Dateien zu lesen
		zeile = f.readline()
		if len(zeile) == 0:
			break
		time.sleep(2)
		print zeile,
finally:
	f.close()
	print 'Raeume auf... Datei geschlossen.'

#!/usr/bin/python

gedicht = '''\
Programmieren mit Elan
und die Arbeit wird getan,
willst du Spass haben daran:
	Nimm Python!
'''

f = file('gedicht.txt', 'w') # "w" = Schreiben
f.write(gedicht) # schreibe den Text in die Datei
f.close() # schliesse die Datei

f = file('gedicht.txt') # kein Modus bedeutet "r" = Lesen
while True:
	line = f.readline()
	if len(line) == 0: # eine leere Zeile bedeutet Dateiende (EOF)
		break
	print line, # das Komma dient zur Unterdrueckung des Zeilenvorschubs
f.close() # schliesse die Datei

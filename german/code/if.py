#!/usr/bin/python

zahl = 23
geraten = int(raw_input('Geben Sie eine ganze Zahl ein : '))

if geraten == zahl:
	print 'Glueckwunsch, Sie haben es erraten.' # ein neuer Block beginnt hier
	print "(Aber Sie gewinnen leider keinen Preis!)" # und hier hoert er auf
elif geraten < zahl:
	print 'Nein, die Zahl ist etwas hoeher.' # noch ein Block
	# Sie koennen in dem Block tun, was sie wollen ...
else:
	print 'Nein, die Zahl ist etwas niedriger.'
	# hierhin gelangt man, wenn geraten > zahl ist

print 'Fertig.'
# Diese letzte Anweisung wird immer am Ende nach der if-Anweisung ausgefuehrt

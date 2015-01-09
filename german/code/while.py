#!/usr/bin/python

zahl = 23
weiter = True

while weiter:
	geraten = int(raw_input('Geben Sie eine ganze Zahl ein : '))

	if zahl == geraten:
		print 'Glueckwunsch, Sie haben es erraten.'
		weiter = False # das fuehrt zum Ende der while-Schleife
	elif geraten < zahl:
		print 'Nein, die Zahl ist etwas hoeher.'
	else:
		print 'Nein, die Zahl ist etwas niedriger.'
else:
	print 'Die while-Schleife wurde beendet.'
	# Hier koennte man noch weitere Dinge tun.

print 'Fertig.'

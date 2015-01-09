#!/usr/bin/python

import sys

def liesdatei(dateiname):
	'''Gib eine Datei auf der Standardausgabe aus.'''
	f = file(dateiname)
	while True:
		zeile = f.readline()
		if len(zeile) == 0:
			break
		print zeile, # beachten Sie das Komma
	f.close()

# das Skript beginnt hier
if len(sys.argv) < 2:
	print 'Es wurden keine Parameter uebergeben.'
	sys.exit()

if sys.argv[1].startswith('--'):
	option = sys.argv[1][2:]
	# hole sys.argv[1], aber ohne die ersten beiden Zeichen
	if option == 'version':
		print 'Version 1.2'
	elif option == 'hilfe':
		print '''\
Dieses Programm gibt Dateien auf der Standardausgabe aus.
Es kann eine beliebige Anzahl von Dateien angegeben werden.
Als Optionen koennen angegeben werden:
  --version : Gibt die Versionsnummer aus
  --hilfe   : Gibt diese Hilfe aus'''
	else:
		print 'Unbekannte Option.'
	sys.exit()
else:
	for dateiname in sys.argv[1:]:
		liesdatei(dateiname)

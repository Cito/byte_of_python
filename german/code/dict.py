#!/usr/bin/python

# 'ab' steht kurz fuer 'A'dress'b'uch

ab = {		'Swaroop'   : 'swaroopch@byteofpython.info',
		'Larry'     : 'larry@wall.org',
		'Matsumoto' : 'matz@ruby-lang.org',
		'Spammer'   : 'spammer@hotmail.com'
	}

print "Swaroops Adresse ist %s" % ab['Swaroop']

# Ein Schluessel/Wert-Paar hinzufuegen
ab['Guido'] = 'guido@python.org'

# Ein Schluessel/Wert-Paar loeschen
del ab['Spammer']

print '\nEs gibt %d Kontakte im Adressbuch\n' % len(ab)

for name, adresse in ab.items():
	print '%s hat die Adresse %s' % (name, adresse)

if 'Guido' in ab: # oder: ab.has_key('Guido')
	print "\nGuidos Adresse ist %s" % ab['Guido']

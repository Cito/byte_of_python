#!/usr/bin/python

# Dies ist meine Einkaufsliste
einkaufsliste = ['Aepfel', 'Mangos', 'Karotten', 'Bananen']

print 'Ich habe', len(einkaufsliste), 'Dinge einzukaufen.'

print 'Diese Dinge sind:', # Beachten Sie das Komma am Zeilenende
for ding in einkaufsliste:
	print ding,

print '\nIch muss auch Reis einkaufen.'
einkaufsliste.append('Reis')
print 'Meine Einkaufsliste ist jetzt:'
print einkaufsliste

print 'Jetzt werde ich meine Einkaufsliste sortieren.'
einkaufsliste.sort()
print 'Die sortierte Einkaufsliste ist:'
print einkaufsliste

print 'Zuerst werde ich', einkaufsliste[0], 'kaufen.'
altesding = einkaufsliste[0]
del einkaufsliste[0]
print 'Ich habe', altesding, 'gekauft.'
print 'Meine Einkaufsliste ist jetzt:'
print einkaufsliste

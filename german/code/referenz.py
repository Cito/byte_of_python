#!/usr/bin/python

print 'Einfache Zuweisung'
einkaufsliste = ['Aepfel', 'Mangos', 'Karotten', 'Bananen']
meineliste = einkaufsliste
# meineliste ist nur ein anderer Name, der auf das gleiche Objekt zeigt!

# Ich habe den ersten Posten gekauft und entferne ihn daher von der Liste
del einkaufsliste[0]

print 'einkaufsliste ist', einkaufsliste
print 'meineliste ist', meineliste
# Beachten Sie, dass sowohl einkaufsliste als auch meineliste
# die gleiche Liste ohne die 'Aepfel' ausgeben, was bestaetigt,
# dass sie auf das gleiche Objekt zeigen

print 'Kopie mittels Teilbereichsoperation'
meineliste = einkaufsliste[:] # auf diese Weise wird die gesamte Liste kopiert
del meineliste[0] # entferne das erste Element

print 'einkaufsliste ist', einkaufsliste
print 'meineliste ist', meineliste
# Beachten Sie, dass die beiden Listen nun unterschiedlich sind

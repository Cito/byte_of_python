#!/usr/bin/python

einkaufsliste = ['Aepfel', 'Mangos', 'Karotten', 'Bananen']

# Indizierungs-Operation
print 'Position 0 ist', einkaufsliste[0]
print 'Position 1 ist', einkaufsliste[1]
print 'Position 2 ist', einkaufsliste[2]
print 'Position 3 ist', einkaufsliste[3]
print 'Position -1 ist', einkaufsliste[-1]
print 'Position -2 ist', einkaufsliste[-2]

# Teilbereichs-Operation auf einer Liste
print 'Position 1 bis 3 ist', einkaufsliste[1:3]
print 'Position 2 bis Ende ist', einkaufsliste[2:]
print 'Position 1 bis -1 ist', einkaufsliste[1:-1]
print 'Position Anfang bis ist', einkaufsliste[:]

# Teilbereichs-Operation auf einem String
name = 'swaroop'
print 'Zeichen 1 bis 3 ist', name[1:3]
print 'Zeichen 2 bis Ende ist', name[2:]
print 'Zeichen 1 bis -1 ist', name[1:-1]
print 'Zeichen Anfang bis Ende', name[:]

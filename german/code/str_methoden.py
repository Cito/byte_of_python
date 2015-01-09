#!/usr/bin/python

name = 'Swaroop' # Dies ist ein String-Objekt

if name.startswith('Swa'):
	print 'Ja, der String beginnt mit "Swa".'

if 'a' in name:
	print 'Ja, er enthält den String "a".'

if name.find('war') != -1:
	print 'Ja, er enthält den String "war".'

trennzeichen = '_*_'
meineliste = ['Brasilien', 'Russland', 'Indien', 'China']
print trennzeichen.join(meineliste)

#!/usr/bin/python

class Person:
	'''Stellt eine Person dar.'''
	bevoelkerung = 0

	def __init__(self, name):
		'''Initialisiert die Daten der Person.'''
		self.name = name
		print '(Initialisiere %s)' % self.name

		# Wenn diese Person erzeugt wird,
		# traegt er/sie zur Bevoelkerung bei
		Person.bevoelkerung += 1

	def __del__(self):
		'''Ich sterbe.'''
		print '%s verabschiedet sich.' % self.name

		Person.bevoelkerung -= 1

		if Person.bevoelkerung == 0:
			print 'Ich bin der letzte.'
		else:
			print 'Es gibt noch %d Leute.' % Person.bevoelkerung

	def sagHallo(self):
		'''Begruessung durch die Person.

		Das ist wirklich alles, was hier geschieht.'''
		print 'Hallo, mein Name ist %s.' % self.name

	def wieViele(self):
		'''Gibt die aktuelle Bevoelkerungszahl aus.'''
		if Person.bevoelkerung == 1:
			print 'Ich bin ganz allein hier.'
		else:
			print 'Es gibt hier %d Leute.' % Person.bevoelkerung

swaroop = Person('Swaroop')
swaroop.sagHallo()
swaroop.wieViele()

kalam = Person('Abdul Kalam')
kalam.sagHallo()
kalam.wieViele()

swaroop.sagHallo()
swaroop.wieViele()

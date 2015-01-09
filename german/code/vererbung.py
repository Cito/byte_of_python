#!/usr/bin/python

class SchulMitglied:
	'''Repraesentiert ein beliebiges Mitglied der Hochschule.'''
	def __init__(self, name, alter):
		self.name = name
		self.alter = alter
		print '(SchulMitglied %s initialisiert)' % self.name

	def auskunft(self):
		'''Gib Auskunft ueber das Mitglied.'''
		print 'Name: "%s" Alter: "%s"' % (self.name, self.alter),

class Dozent(SchulMitglied):
	'''Repraesentiert einen Dozenten der Hochschule.'''
	def __init__(self, name, alter, gehalt):
		SchulMitglied.__init__(self, name, alter)
		self.gehalt = gehalt
		print '(Dozent %s initialisiert)' % self.name

	def auskunft(self):
		SchulMitglied.auskunft(self)
		print 'Gehalt: "%d Euro"' % self.gehalt

class Student(SchulMitglied):
	'''Repraesentiert einen Studenten der Hochschule.'''
	def __init__(self, name, alter, note):
		SchulMitglied.__init__(self, name, alter)
		self.note = note
		print '(Student %s initialisiert)' % self.name

	def auskunft(self):
		SchulMitglied.auskunft(self)
		print 'Letzte Pruefungsnote: "%1.1f"' % self.note

d = Dozent('Mrs. Shrividya', 40, 30000)
s = Student('Swaroop', 22, 1.7)

print # gib eine Leerzeile aus

mitglieder = [d, s]
for mitglied in mitglieder:
	mitglied.auskunft() # geht bei Dozenten und Studenten

#!/usr/bin/python

class Person:
	def __init__(self, name):
		self.name = name
	def sagHallo(self):
		print 'Hallo, mein Name ist', self.name

p = Person('Swaroop')
p.sagHallo()

# Dieses kurze Beispiel kann auch als
# Person('Swaroop').sagHallo() geschrieben werden.
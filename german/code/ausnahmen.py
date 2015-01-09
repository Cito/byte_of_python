#!/usr/bin/python

class KurzeEingabeAusnahme(Exception):
	'''Eine benutzerdefinierte Ausnahmeklasse.'''
	def __init__(self, laenge, mindestens):
		Exception.__init__(self)
		self.laenge = laenge
		self.mindestens = mindestens

try:
	s = raw_input('Geben Sie etwas ein --> ')
	if len(s) < 3:
		raise KurzeEingabeAusnahme(len(s), 3)
	# Hier kann man ganz normal mit der Arbeit fortfahren
except EOFError:
	print '\nWarum haben Sie die Eingabe abgebrochen?'
except KurzeEingabeAusnahme, x:
	print 'KurzeEingabeAusnahme: Eingabe hatte die Laenge %d,' \
		' gefordert war mindestens %d.' % (x.laenge, x.mindestens)
else:
	print 'Es wurde keine Ausnahme ausgeloest.'

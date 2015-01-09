#!/usr/bin/python

import cPickle as p
#import pickle as p

einkaufsdatei = 'einkaufsliste.data' # Datei, in der wir das Objekt speichern

einkaufsliste = ['Aepfel', 'Mangos', 'Karotten']

# Schreibe in die Datei
f = file(einkaufsdatei, 'w')
p.dump(einkaufsliste, f) # speichere das Objekt in der Datei
f.close()

del einkaufsliste # loesche die einkaufsliste

# Lies die Einkaufsliste aus der Datei wieder ein
f = file(einkaufsdatei)
gespeicherteliste = p.load(f)
print gespeicherteliste

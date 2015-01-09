#!/usr/bin/python

zoo = ('Wolf', 'Elefant', 'Pinguin')
print 'Die Zahl der Tiere im Zoo ist', len(zoo)

neuer_zoo = ('Affe', 'Delfin', zoo)
print 'Die Zahl der Tiere im neuen Zoo ist', len(neuer_zoo)
print 'Alle Tiere im neuen Zoo sind', neuer_zoo
print 'Die aus dem alten Zoo uebernommenen Tiere sind', neuer_zoo[2]
print 'Das letzte aus dem alten Zoo uebernommene Tier ist ein', neuer_zoo[2][2]

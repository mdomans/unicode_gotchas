# -*- coding:utf-8 -*-
#!/usr/bin/env python
# Bartek zadał pytanie:
# Q: Dlaczego u w 6 jest konieczne, a nie jest konieczne w 24?

s = "%s" % u"żółw".encode('utf-8')
print s, type(s)

"""
tutaj mamy obiekt unicode, kodujemy go do utf-8 i wstawiamy do bytestringa, wszystko ok
ale encode nie jest konieczne
"""
s = '%s' % u"żółw"
print s, type(s)

"""
Co tu się stało? Jeśli mamy operacją na obiektach str i unicode, Python automatycznie próbuje zrobić Unicode z naszego
stringa używając kodeka ASCII, dlatego dopiero to nie zadziała:
"""

print "żó" + u"łw"


s2 = "%s".encode('utf-8') % "żółw"
print s2

"""
a tu mamy bytestring i:
1. wykonujemy encode do UTF-8, ponieważ jest to string w ASCII to codec castuje go do Unicode
2. kodujemy go do utf-8, mamy znowu str
3. Wstawiamy obiekt 'żółw', ale zanim to wstawimy, interpreter robi automatyczna konwersję

ergo, tak to naprawdę wygląda:
"""

s2 = "%s".encode('utf-8') % u"żółw".encode('utf-8')
print s2.decode('utf-8')

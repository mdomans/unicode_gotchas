#!/usr/bin/env python

# Q: Dlaczego uruchomienie tego skryptu nie zadziała?
# A: Nie zadeklarowano kodowania pliku py.
#    Dodaj # -*- coding:utf-8 -*- w pierwszej linii pliku
#
# Typowy output:
# $ python 01.py
# SyntaxError: Non-ASCII character '\xc5' in file ./me.py on line 3, but no
# encoding declared; see http://www.python.org/peps/pep-0263.html for details

print u"żółw"

"""
A wyjaśnienie jest takie:
u to literał, a więc u"żółw" oznacza obiekt Unicode, ale ponieważ nie mamy ustawionego kodowania,
interpreter nie wie jak przemielić 'ż' na unicode 'ż'

bo print u"żółw" oznacza:

1. masz tu zestaw znaków z mojego kompa: żółw
2. skonwertuj mi to na obiekt unicode
3. wyrzuć go na konsolę

a interpreter:
1. otwiera plik skryptu
2. nie widzi kodowania, zakłada więc że każdy znak w pliku to ASCII
3. wywala się, bo literka ż nie jest w ASCII

"""
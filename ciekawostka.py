#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
#
# Czemu mogę zrobić tak w konsoli, np. w ipythonie?

def a():
    c = 'ś'
    return c

#
# Hmmmmmm, spójrzmy na bytecode
#   2           0 LOAD_CONST               1 ('\xc5\x9b')
#               3 STORE_FAST               0 (c)
#
#   3           6 LOAD_FAST                0 (c)
#               9 RETURN_VALUE
#
# Czyli ipython tak naprawdę robi z naszym kodem to:

def a():
    c = u"ś".encode('utf-8')
    return c

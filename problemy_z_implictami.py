#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Jak to sobie już opowiadaliśmy, Python dużo rzeczy konwertuje za nas
#
# Czy mogą być z tego problemy?

# co dostaniemy?

print "ś"[-1]

# ponieważ Python robi nam pod maską sztuczkę, a potem to próbuje odwrócić
# ja dostałem: ?

# Co zrobić żeby było dobrze?

print u"ś"[-1]

# A jakie są implicity

print 'text' == u'text'


# -*- coding:utf-8 -*-
#!/usr/bin/env python

# Q: Dlaczego przepuszczenie tego skryptu przez rurę nie zadziała?
# A: Nie wiem ale zakodowanie do utf-8 rozwiązuje problem.
#    print u"żółw".encode('utf-8')
#
# Typowy output:
# $ python 02.py | sort
# Traceback (most recent call last):
#   File "02.py", line 12, in <module>
#     print u"żółw"
# UnicodeEncodeError: 'ascii' codec can't encode characters in
# position 0-2: ordinal not in range(128)

print u"żółw"


"""

Wyjaśnienie:

Kiedy robimy:

$ python 02.py | sort

to interpreter w naszym imieniu łapie obiekt znany jako PIPE i próbuje do niego pisać

PIPE to bufor znakowy, co oznacza że tak naprawdę dzieje się to:

import os
r, w = os.pipe()
os.write(w, u"żółw".encode('ascii'))


"""
# -*- coding:utf-8 -*-
#!/usr/bin/env python
#
# Q: Ten kod zadziała bez rury. Jak go zmodyfikować żeby działał przez rurę?
# A:
#    for s in list_of_strings_i_dont_control:
#        if issubclass(s.__class__, unicode):
#            print s.encode('utf-8')
#        else:
#            print s
#
# Typowy output:
#
# $ python 05.py
# żółw
# ...
# $ python 05.py | sort
# Traceback (most recent call last):
#   File "05.py", line 15, in <module>
#     s = s.encode('utf-8')
# UnicodeDecodeError: 'ascii' codec can't decode byte 0xc5 in position 0: ordinal not in range(128)
# żółw
# żółw

list_of_strings_i_dont_control = [
    u"żółw",
    "żółw",
    '\xc5\xbc\xc3\xb3\xc5\x82w',
    u'\u017c\xf3\u0142w',
    # i dwa totalnie zepsute stringi, których wyświetlic sie nie da
    # u'\xc5\xbc\xc3\xb3\xc5\x82w',
    # '\u017c\xf3\u0142w'
]


for s in list_of_strings_i_dont_control:
    print s.encode('utf-8')


"""
Już tłumaczyłem :D
"""
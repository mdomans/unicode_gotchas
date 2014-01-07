# -*- coding:utf-8 -*-
#!/usr/bin/env python

# Q: Czy jest różnica pomiędzy print a sys.stdout.write?
# A: Wygląda na to, że nie ma (poza \n na końcu w princie) ale nie jestem pewien
import sys

s = u"żółw".encode('utf-8')

print s
sys.stdout.write(s)

"""
nie ma
"""
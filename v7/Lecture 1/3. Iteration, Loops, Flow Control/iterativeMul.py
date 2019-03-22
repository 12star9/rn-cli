# -*- coding: utf-8 -*-
"""
Created on Sat Aug 25 2018

"""

x = 5
ans = 0
itersLeft = x
while (itersLeft != 0):
    ans = ans + x
    itersLeft = itersLeft - 1
print(str(x) + '*' + str(x) + ' = ' + str(ans))

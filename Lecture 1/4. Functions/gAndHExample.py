# -*- coding: utf-8 -*-
"""
Created on Sat Aug 25 2018

"""

def g(x):
    def h():
        x = 'abc'
    x = x + 1
    print('in g(x): x =', x)
    h()
    return x

x = 3
z = g(x)

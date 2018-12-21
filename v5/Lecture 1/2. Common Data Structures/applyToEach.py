# -*- coding: utf-8 -*-
"""
Created on Sat Aug 25 2018

"""

def applyToEach(L, f):
    """assumes L is a list, f a function
       mutates L by replacing each element,
       e, of L by f(e)"""
    for i in range(len(L)):
        L[i] = f(L[i])
        

def applyFuns(L, x):
    for f in L:
         print(f(x))


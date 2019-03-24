# -*- coding: utf-8 -*-
"""
Created on Sat Aug 25 2018

"""

def mult_list_recur(L):
    if len(L) == 1:
        return L[0]
    else:
        return L[0]*mult_list_recur(L[1:])

print(mult_list_recur([1,3,5,7,9]))
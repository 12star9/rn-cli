# -*- coding: utf-8 -*-
"""
Created on Sat Aug 25 2018

"""

mysum = 0
for i in range(5, 11, 2):
    mysum += i
    if mysum == 5:
        break 
print(mysum)

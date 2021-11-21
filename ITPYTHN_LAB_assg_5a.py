# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 10:26:34 2020

@author: 91912
"""
'''AUTOMORPHIC NUMBERS'''

import math as m
print('The automorphic numbers within the given range are : ')
for i in range(11,101):
    sq=i**2
    n=int(m.log10(i))+1
    num=int(sq%(m.pow(10,n)))
    if(num==i):
        print(num,end=' ')
        
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 11:10:08 2021

@author: 91912
"""

import math as m

x = int(input("Enter  a number: "))
try:
    res = m.sqrt(x)
    print(res)
except:
    print("Negative: ")

# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 10:48:07 2021

@author: 91912
"""

try:
    a = input("Enter the value of a: ")
    b = input("Enter the value of b: ")
    if(a.isdigit() and b.isdigit()):
        print("Sum of a and b = ", int(a)+int(b))
    else:
        raise Exception
except:
    print("Sorry! Non Number Input")

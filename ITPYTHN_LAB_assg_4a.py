# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 10:31:19 2020

@author: acer
"""

''' POWER OF AN NUMBER USING LOOP AND BREAK'''
num = int(input("Enter any positive number : \n"))
exp = int(input("Enter exponent value : \n"))
p = 1
for i in range(1, exp+1):
    p = p * num   
print("The result is : ",p)
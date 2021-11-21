# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 11:50:38 2020

@author: acer
"""
'''Leap Year'''
year=int(input("Enter a year : "))
if year%4==0:
    if year%100==0:
        if year%400==0:
            print("Woaaah......It's a Leap Year")
        else:
             print("Nope.... It's NOT a Leap Year")
    else:
         print("Woaaah......It's a Leap Year")
else:
    print("Nope.... It's NOT a Leap Year")         

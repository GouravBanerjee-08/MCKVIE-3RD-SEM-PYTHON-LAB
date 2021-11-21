# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 10:49:34 2020

@author: acer
"""

'''FIBONACCI SERIES'''
num=int(input('Enter the number of terms for the Fibonacci Series : '))
a,b=0,1
count=0
if(num<=0):
    print('Enter a natural number: ')
else:
    while(count<num):
        print(a,end=' ')
        s=a+b
        a=b
        b=s
        count+=1
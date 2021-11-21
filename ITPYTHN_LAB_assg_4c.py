# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 11:10:23 2020

@author: acer
"""
'''PRIME NUMBERS'''
s=eval(input('Enter start of the range : '))
e=eval(input('Enter end of the range : '))
for i in range(s,e+1):
   if i > 1:
      for n in range(2, (i//2+1)):
         if(i%n)==0:
            break
      else:
         print(i,end=' ')
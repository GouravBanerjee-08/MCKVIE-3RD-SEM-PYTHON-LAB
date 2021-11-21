# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 11:39:37 2020

@author: acer
"""
'''Greatest among 3 Number's '''
x=int(input("Enter the value of 1st Number: "))
y=int(input("Enter the value of 2nd Number: "))
z=int(input("Enter the value of 3rd Number: "))
 
if (x>y) and (x>z):
    greatest=x
elif(y>x) and (y>z):
    greatest=y
else:
    greatest=z
    
print("The greatest Number is ",greatest)
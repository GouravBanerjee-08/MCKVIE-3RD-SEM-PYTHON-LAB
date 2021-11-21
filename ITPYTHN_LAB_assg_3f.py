# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 12:11:29 2020

@author: acer
"""
''' Electric Bill'''
unit_consumed=float(input("Enter the number of units consumed by the customer : "))
if(unit_consumed>=0 and unit_consumed<=200):
    charge=0.50*unit_consumed
elif(unit_consumed>=201 and unit_consumed<=400):
    charge=100+0.65*unit_consumed
elif(unit_consumed>=401 and unit_consumed<=600):
    charge=200+0.80*unit_consumed
else:
    charge=300+1.00*unit_consumed
print("The amount to be Paid to the Customer is: Rs.",charge)
    
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 10:54:06 2020

@author: acer
"""
''' Basic Salary of an Employee'''
             
             
BasicPay=int(input("The Basic salary:"))

AGP=50/100*BasicPay

MergedBasic=BasicPay+AGP

DA=50/100*MergedBasic

HRA=12/100*MergedBasic

Total=MergedBasic+DA+HRA

print("The Total salary of an Employee: ",Total)

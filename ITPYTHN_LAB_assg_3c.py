# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 12:19:51 2020

@author: acer
"""
'''Quadratic Equation'''
import math as c
import cmath as m
a=float(input("Enter the Value of a : "))
b=float(input("Enter the Value of b : "))
c=float(input("Enter the Value of c : "))
dis=(b*2)-(4*a*c)
if dis==0:
    r=(-b)//(2*a)
    print("The roots are Real and Equal. Roots are =",r,"and",r)
elif dis>0:
    r1=(-b+math.sqrt(dis))/(2*a)
    r2=(-b-math.sqrt(dis))//(2*a)
    print("The roots are Real and Distinct roots. Roots are =",r1,"and",r2)
else:
    x=(-b)/(2*a)
    y=(m.sqrt(dis))/2*a
    print("The roots are Imaginary Roots.Roots are =",(x+y),"and",(x-y))
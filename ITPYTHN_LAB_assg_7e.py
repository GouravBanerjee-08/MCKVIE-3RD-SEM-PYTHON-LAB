# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 10:58:11 2021

@author: 91912
"""

s=input("enter the string : ")
k=0
f=1
l=len(s)
for i in range(l):
    if(s[i]=='('):
        k=k+1
    elif(s[i]==')'):
        k=k-1
    if(k<0):
        f=0
        break

if(f==1):
    print("TRUE")
else:
    print("FALSE")
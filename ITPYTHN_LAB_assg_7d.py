# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 10:20:16 2021

@author: 91912
"""

s=input("enter the email address: ")
l=len(s)
start=0
end=0
for i in range(l):
    if(s[i]=='@'):
        start=i+1
    if(s[i]=='.'):
        end=i
for i in range(start,end):
    print(s[i], end="")
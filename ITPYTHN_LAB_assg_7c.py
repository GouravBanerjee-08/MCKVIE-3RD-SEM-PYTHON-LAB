# -*- coding: utf-8 -*-
"""
Created on Fri Jan  8 11:32:04 2021

@author: 91912
"""

str1=input('Please enter words seperated by commas : ')
str2=str1.split(',')
l=len(str2)
for i in range(l-1):
    for j in range (l-i-1):
        if(str2[j]>str2[j+1]):
            str2[j],str2[j+1]=str2[j+1],str2[j]
print("The Sorted words in sequence are : ",end='')
for i in range (l-1):
    print(str2[i],end=',')
print(str2[l-1])
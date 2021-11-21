# -*- coding: utf-8 -*-
"""
Created on Fri Jan  8 11:24:07 2021

@author: 91912
"""

str1=input('Please enter the sentence : ')
upper=lower=0
for i in range(len(str1)):
    if(str1[i].isupper()):
        upper+=1
    elif(str1[i].islower()):
        lower+=1
print(upper,lower)
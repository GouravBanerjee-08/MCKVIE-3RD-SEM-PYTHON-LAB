# -*- coding: utf-8 -*-
"""
Created on Fri Jan  8 11:32:04 2021

@author: 91912
"""
str1=input('Enter the sentence : ')
str2=str1.split('\\n')
for i in str2[1:]:
    print(i.upper())
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 11:59:57 2021

@author: 91912
"""

fptr = open("11d.txt", "r")

line = (fptr.readlines())
for i in range(len(line)):
    print(line[i], end = "")
fptr.close()
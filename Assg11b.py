# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 11:18:09 2021

@author: 91912
"""

fptr = open("11b.txt","w")

n = int(input("Enter the no. upto which prime nos. are to be printed: "))

for n in range(2,n):
        for i in range(2,n):
            if(n%i==0):
                break
        else:
            fptr.write(str(n))
            fptr.write(" ")

fptr.close()

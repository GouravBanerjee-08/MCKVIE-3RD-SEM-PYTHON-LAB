# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 11:08:04 2020

@author: 91912
"""

import numpy as np
n=int(input('Enter the Length of an Array : '))
a=np.zeros((n),dtype='int')
print ('Enter the elements in arrays : ')
for i in range(0,n):
    a[i]=int(input(""))
m1=a[0]
m2=a[0]
for i in range(0,n):
    if (a[i]>m1):
        m1=a[i]
    if(a[i]<m2):
        m2=a[i]
print('MAX ELEMENT is : ',m1)
print('MIN ELEMENT is : ',m2)

r=int(input('Enter the number of Rows : ' ))
c=int(input('Enter the Number of Columns : '))
b=np.zeros((r,c),dtype='int')
print ('Enter the elements in the 2-D array : ')
for i in range(0,r):
    for j in range(0,c):
        b[i,j]=int(input(""))
max_1=b[0,0]
min_1=b[0,0]
for i in range(0,r):
    for j in range(0,c):
        if (b[i,j]>max_1):
            max_1=b[i,j]
        if (b[i,j]<min_1):
            min_1=b[i,j]
print('MAX ELEMENT in 2D Array is : ',max_1)
print('MIN ELEMENT in 2D Array is : ',min_1)
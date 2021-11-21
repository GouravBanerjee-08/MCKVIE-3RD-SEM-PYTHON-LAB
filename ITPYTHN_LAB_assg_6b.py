# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 11:50:50 2020

@author: 91912
"""

import numpy as np
P=np.empty(6,dtype=int)
Q=np.empty(4,dtype=int)
R=np.empty(10,dtype=int)
print("Enter the elements of P array : ")
for i in range(0,6):
    P[i]=int(input())
print("Enter the Elements of Q array : ")
for i in range(0,4):
    Q[i]=int(input())
i,j,k=0,0,0
for i in range (0,6):
    R[k]=P[i]
    i=i+1
    k=k+1
for j in range (0,4):
    R[k]=Q[j]
    j=j+1
    k=k+1
print('The resultant array is : ',R)
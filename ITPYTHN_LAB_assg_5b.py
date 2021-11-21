# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 10:45:09 2020

@author: 91912
"""
'''SPECIAL NUMBERS OR KRISHNAMURTHY NUMBERS'''

print('The special numbers are : ')
for num in range(100,1000):
    n=num
    s=0
    while(num>0):
        fact=1
        r=num%10
        num=num//10
        for i in range(1,r+1):
            fact=fact*i
        s=s+fact
    if(s==n):
        print(n)
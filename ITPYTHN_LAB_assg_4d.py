# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 11:19:35 2020

@author: acer
"""
'''PALINDROME'''
num=int(input('Enter the number : '))
n=num
rev=0
while(n!=0):
    rem=n%10
    n=n//10
    rev=rev*10+rem
if(rev==num):
    print('Congratulations,It is a palindrome.')
else:
    print(' Sorry, It is not a palindrome.')
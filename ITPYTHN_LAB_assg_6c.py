# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 11:15:22 2020

@author: 91912
"""

'''import numpy as np
while(1):
    print("1.Bubble Sort")
    print("2.Selection Sort")
    print("3.Insertion Sort")
    print("4.Exit")
    uinput = int(input(""))
    if(uinput==1):
        a=int(input("Enter the number of elements in array : "))
        x=np.zeros((a),dtype=int) 
        print("\nEnter the elements in array : ")
        for i in range (0,a):
            x[i]=int(input(""))
        for m in range (0,a):
                for n in range (a-m-1):
                    if x[n] > x[n+1]:
                        temp = x[n]
                        x[n] = x[n+1]
                        x[n+1] = temp
        print(x)
    if(uinput==2):
        a=int(input("Enter the number of elements in array : "))
        x=np.zeros((a),dtype=int) 
        print("\nEnter the elements in array : ")
        for i in range (0,a):
            x[i]=int(input(""))
        for m in range (0,a):
            minpos=m
            for n in range (m,a):
                if x[n] < x[minpos]:
                    minpos = n
            temp = x[m]
            x[m] = x[minpos]
            x[minpos] = temp    
        print(x)
    if(uinput==3):
        a=int(input("Enter the number of elements in array : "))
        x=np.zeros((a),dtype=int) 
        print("\nEnter the elements in array : ")
        for i in range (0,a):
            x[i]=int(input(""))
        for m in range (0,a):
            current_ele = x[i]
            pos = i
            while(current_ele < x[pos-1]) and pos>0:
                x[pos] = x[pos-1]
                pos = pos -1
            x[pos] = current_ele
        print(x)
    if(uinput==4):
        break'''
import numpy as np
n=eval(input('Enter array size : '))
a=np.zeros((n),dtype='int')
print("Enter array elements : ")
for i in range(0,n):
    a[i]=int(input(""))
print("press 1 for bubble sort,press 2 for selection sort and press 3 for insertion sort")
ch=eval(input('Enter your choice : '))

if(ch==1):
    for i in range(0,n):
          for j in range(0,n-i-1):
            for k in range(0,n):
                print(a[k],end=' ')
            print()
            if(a[j]>a[j+1]):
                temp=a[j]
                a[j]=a[j+1]
                a[j+1]=temp
    print('The sorted array is : ')
    for i in range(0,n):
        print(a[i],end=' ')

elif(ch==2):
   for i in range(0,n):
      min=a[i]
      loc=i
      for k in range(0,n):
          print(a[k],end=' ')
      print()
      for j in range(i+1,n):
          if(a[j]<min):
              min=a[j]
              loc=j
      if(loc!=i):
         temp=a[loc]
         a[loc]=a[i]
         a[i]=temp
   print('The sorted array is : ')
   for i in range(0,n):
       print(a[i],end=' ')

elif(ch==3):
    for i in range(1, n):
        key=a[i]
        j=i-1
        for k in range(0,n):
           print(a[k],end=' ')
        print()
        while (j>=0 and key<a[j]) : 
                a[j+1]=a[j]
                j -= 1
        a[j+1]=key
    print('The sorted array is : ')
    for i in range(0,n):
        print(a[i],end=' ')

else:
   print('WRONG CHOICE')
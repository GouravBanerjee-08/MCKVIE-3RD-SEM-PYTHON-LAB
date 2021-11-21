'''import numpy as np
while(1):
    print("1.Linear Search")
    print("2.Binary Search")
    print("3.Exit")
    uinput = int(input(""))
    if(uinput==1):
        a=int(input("Enter the number of elements in array : "))
        x=np.zeros((a),dtype=int) 
        print("\nEnter the elements in array : ")
        for i in range (0,a):
            x[i]=int(input(""))
        key = int(input("Enter Number to Search::"))
        for i in range (a):
            if x[i]==key:
                print("Element Found at :",i)
                break
        else:
            print("Element not Found")
    if(uinput==2):
        a=int(input("Enter the number of elements in array : "))
        x=np.zeros((a),dtype=int) 
        print("\nEnter the elements in array : ")
        for i in range (0,a):
            x[i]=int(input(""))
        key = int(input("Enter Number to Search :"))
        l = 0
        u = a-1
        
        while l<= u:
            mid =(l+u)//2
            if x[mid]==key:
                print("Element Found at :",mid)
                break
            else:
                if x[mid]< key:
                    l = mid +1
                else:
                    u = mid-1
        else:
            print("Element Not Found")
    if(uinput==3):
        break'''

import numpy as np

print("press 1 for linear search and 2 for binary search")
n=int(input("enter your choice:"))
size=int(input("enter the size of array:"))
x=np.zeros((size),dtype=int)
print("enter the elements")
for i in range (0,size):
    x[i]=int(input(" "))
key=int(input("enter the element to be searched:"))
if(n==1):
    f=0
    for i in range(0,size):
        if(x[i]==key):
            print("found at index:",end=' ')
            print(i)
            f=1
            break
    if(f==0):
        print("not found")
        
elif(n==2):
    l=0
    r=size
    f=0
    while(i<r):
        mid=(l+r)//2
        if(x[mid]==key):
            print("found at index:",mid)
            f=1
            break
        elif(x[mid]>key):
            r=mid-1
        else:
            l=mid+1
    if(f==0):
        print("not found")

else:
   print('WRONG CHOICE')
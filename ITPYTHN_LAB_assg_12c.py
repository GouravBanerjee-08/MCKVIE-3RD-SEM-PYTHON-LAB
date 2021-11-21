# -*- coding: utf-8 -*-
"""
Created on Fri Feb 12 10:57:20 2021

@author: 91912
"""

class Point:
    x=y=0
    
    def __init__(self,x,y):
        self.x = x
        self.y = y
        
    def Display(self):
        print("The Coordinate of x is : ",self.x)
        print("The Coordinate of y is : ",self.y)
        
    def Translate(self,x,y):
        self.y = self.y+x
        self.x = self.x+y
        
x = int(input("Enter the value of x : "))
y = int(input("Enter the value of y : "))
ob = Point(x,y)
ob.Display()
print("The Translate value")
ob.Translate(x,y)
ob.Display()
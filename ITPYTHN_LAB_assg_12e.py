# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 10:47:53 2021

@author: acer
"""
class Shape:
    colour= ""
    
    def __init__(self,c):
        self.colour=c

class Rectangle(Shape):
    length  = 0.0
    breadth = 0.0
    
    def __init__(self, l, br, co):
        self.length  = l
        self.breadth = br
        self.colour = co        
        
    def Calc_Area(self):
            Area = (self.length)*(self.breadth)
            return Area
        
class Triangle(Shape):
    height  = 0.0
    base    = 0.0
    
    def __init__(self, h, ba, col):
        self.height  = h
        self.base = ba
        self.colour = col
        
    def Calc_Area(self):
            Area = 0.5*(self.base)*(self.height)
            return Area
        
a = eval(input(" Enter the Length of the Rectangle : "))
b = eval(input(" Enter the Breadth of the Rectangle : "))
c = input(" Enter the Colour of the Rectangle : ")
ob1=Rectangle(a,b,c)
print("Area of the Rectangle : ", ob1.Calc_Area())
d = eval(input(" Enter the Height of the Triangle : "))
e = eval(input(" Enter the Base of the Triangle : "))
f = input(" Enter the Colour of the Triangle : ")
ob2= Triangle(d,e,f)
print("Area of the Triangle : ",ob2.Calc_Area())
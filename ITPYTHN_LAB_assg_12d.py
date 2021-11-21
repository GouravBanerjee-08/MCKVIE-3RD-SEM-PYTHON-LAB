# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 10:01:46 2021

@author: acer
"""

class Circle:
    radius=0.0
    def __init__(self,r):
        self.radius = r
        
    def Get_Radius(self):
        x = self.radius
        return x
    
    def Calc_Area(self):
        Area = (3.14)*(self.radius)*(self.radius)
        return Area
    
class Cylinder(Circle):
    height=0.0
    def __init__(self,r,h):
        self.height=h
        self.radius=r
        super().__init__(r)
    def Calc_Area(self):
        Area = (2)*(3.14)*(self.radius)*(self.height)
        return Area

a = eval(input('Enter Radius of your Choice : '))
b = eval(input('Enter Height of your Choice : '))     
ob1 = Cylinder(a,b)
print("The Area of the Cylinder Is : ", ob1.Calc_Area())
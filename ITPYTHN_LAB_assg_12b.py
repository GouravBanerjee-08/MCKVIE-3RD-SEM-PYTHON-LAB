# -*- coding: utf-8 -*-
"""
Created on Fri Feb 12 10:57:15 2021

@author: 91912
"""

class Circle:
    def __init__(self,r):
        self.radius = r
        
    def Get_Radius(self):
        x = self.radius
        return x
    
    def Calc_Area(self):
        Area = (3.14)*(self.radius)*(self.radius)
        return Area
    
ob = Circle(int(input("Enter the Radius : ")))
print("The Given Radius of Circle Is : ", ob.Get_Radius())
print("The Area of the Circle Is : ", ob.Calc_Area())


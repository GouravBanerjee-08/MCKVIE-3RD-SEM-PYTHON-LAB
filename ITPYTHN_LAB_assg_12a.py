# -*- coding: utf-8 -*-
"""
Created on Fri Feb 12 10:56:18 2021

@author: 91912
"""

class Demo:
    str=""
    
    def __init__(self,st):
        self.str=st
        
    def Get_String(self):
        x=self.str
        return x
    def Print_String(self):
        y=(self.str).upper()
        return y
    
    
ob= Demo(str(input("Enter The String : ")))
print("The Given String Is : ", ob.Get_String())
print("The String in Upper case Is : ", ob.Print_String())
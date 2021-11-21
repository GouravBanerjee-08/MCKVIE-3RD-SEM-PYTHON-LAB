# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 11:57:49 2020

@author: acer
"""
'''Attendance'''
no_of_classes_held=int(input("Enter the Number of Classes held : "))
no_of_classes_attended=int(input("Enter the Number of Classes attended : "))
medical=input("Enter the Character(y/n) : ")
per=(no_of_classes_attended/no_of_classes_held)*100
if per<75 and medical=='y':
    print ("You are Allowed to Sit in Exam")
elif per<75 and medical=='n':
    print("Sorry but you are NOT Allowed to Sit in Exam")
    
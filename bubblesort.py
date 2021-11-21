# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 01:49:38 2020

@author: 91912
"""

def bubble_sort (nums):
    for i in range (len(nums)-1,0,-1):
        for j in range(i):
            if nums[j]>nums[j+1]:
                temp=nums[j]
                nums[j]=nums[j+1]
                nums[j+1]=temp
                
                
                
nums=[9,5,2,4,7]
sort(nums)

print(nums)
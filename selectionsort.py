# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 01:57:09 2020

@author: 91912
"""

def selection_sort (nums):
    for i in range (5):
        minpos = i
        for j in range(i,6):
            if nums[j] < nums [minpos]:
                minpos = j
                
                
            temp =nums[i]
            nums[i] = nums[minpos]
            nums[minpos] = temp
            
            
                
nums=[9,5,2,4,7,1]
sort(nums)

print(nums)
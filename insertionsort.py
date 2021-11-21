# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 02:07:26 2020

@author: 91912
"""
def insertion_sort(nums):
	    for i in range(1, len(nums)):
	        anchor = nums[i]
	        j = i - 1
	        while j>=0 and anchor < nums[j]:
	            nums[j+1] = nums[j]
	            j = j - 1
	        nums[j+1] = anchor
	
	
	    nums = [11,9,29]
	    insertion_sort(nums)
	    print(nums)

# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 10:57:38 2021

@author: 91912
"""

import datetime as dt
def date_input_validation(day,month,year):
    isValidDate = True
    try:
        dt.datetime(int(year),int(month),int(day))
    except ValueError:
        isValidDate = False
        if(isValidDate):
            print("Yes")
        else:
            print("No")
date_input_validation(29,2,2019)

    
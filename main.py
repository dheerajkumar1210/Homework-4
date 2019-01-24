# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 14:51:58 2019

@author: dheeraj_kumar
"""

myUniquelist = []

def appendUniqueList(var):
    if var not in myUniquelist:
        myUniquelist.append(var)
        return True
    return False
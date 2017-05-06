#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 15 13:02:56 2017

@author: raktim
"""

while True:
    print("Enter an digit from 1 to 9:")
    num=input()
    var=str(num)
    if(ord(var) in range(48,58)):
        break
print("You are very good")
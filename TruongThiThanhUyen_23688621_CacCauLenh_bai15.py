# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 18:02:31 2024

@author: HP
"""
import math
a=float(input('Nhập số a: '))
b=float(input('Nhập số b: '))
s=((a+b)/(math.pow(a,1/3)+math.pow(b,1/3))-math.pow(a*b,1/3))/math.pow((math.pow(a,1/3)-math.pow(b,1/3)),2)
print(s)
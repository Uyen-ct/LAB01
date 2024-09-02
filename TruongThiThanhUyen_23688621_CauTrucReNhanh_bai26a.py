# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 18:49:47 2024

@author: HP
"""

a=float(input('nhập a: '))
b=float(input('nhập b: '))
c=float(input('nhập c: '))

alpha = a
if a > b:
    a = b
    b = alpha
    
alpha = b
if b > c:
    b = c
    c = alpha
if a > b:
    alpha = a
    a = b
    b = alpha

print("Các số theo thứ tự tăng dần:", a, b, c)

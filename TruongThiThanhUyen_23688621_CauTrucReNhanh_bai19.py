# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 18:40:11 2024

@author: HP
"""

a=int(input('nhập a: '))
b=int(input('nhập b: '))
c=int(input('nhập c: '))
d=int(input('nhập d: '))
if a<b and a<c and a<d:
    print('số có giá trị nhỏ nhất:', a)
elif b<a and b<c and b<d:
    print('số có giá trị nhỏ nhất:',b)
elif c<a and c<b and c<d:
    print('số có giá trị nhỏ nhất:',c)
else:
    print('số có giá trị nhỏ nhất:',d)
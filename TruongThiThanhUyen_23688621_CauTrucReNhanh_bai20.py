# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 19:15:05 2024

@author: HP
"""

a=float(input('nhập a: '))
b=float(input('nhập b: '))
c=float(input('nhập c: '))
if a>b and a>c:
    print('số có giá trị lớn nhất: ',a)
elif b>a and b>c:
    print('số có giá trị lớn nhất: ',b)
else:
    print('số có giá trị lớn nhất: ',c)
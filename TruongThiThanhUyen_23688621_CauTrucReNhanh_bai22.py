# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 19:39:40 2024

@author: HP
"""

a=float(input('nhập a: '))
b=float(input('nhập b: '))
if a==0 and b==0:
    print('phương trình có vô số nghiệm')
elif a==0 and b!=0:
    print('phương trình vô nghiệm')
else:
    print('phương trình có nghiệm duy nhất x=',-b/a)
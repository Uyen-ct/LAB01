# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 19:27:39 2024

@author: HP
"""

a=int(input('nhập a: '))
b=int(input('nhập b: '))
if a>0 and b>0:
    print('Kết quả của chia lấy phần nguyên: ',a//b)
    print('Kết quả của chia lấy phần dư: ',a%b)
else:
    print('Chỉ nhập số nguyên dương: a,b>0')
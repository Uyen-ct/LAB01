# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 17:27:12 2024

@author: HP
"""

# Nhập ngày, tháng, năm sinh
ngay = int(input('Nhập ngày: '))
thang = int(input('Nhập tháng: '))
nam = int(input('Nhập năm: '))
print(f'{ngay}/{thang}/{nam}')
nam_rut_gon = nam % 100
print(f'{ngay}/{thang}/{nam_rut_gon:02d}') 

print(f'{nam}/{thang}/{ngay}')


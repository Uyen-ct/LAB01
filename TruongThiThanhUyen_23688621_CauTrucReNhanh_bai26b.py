# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 19:29:03 2024

@author: HP
"""


a= input('Nhập một số nguyên: ')
chuoiso = list(a)

chuoiso.sort()

chuoi = ''.join(chuoiso)
songuyen = int(chuoi)

print('Số có các chữ số theo thứ tự tăng dần là:', songuyen)


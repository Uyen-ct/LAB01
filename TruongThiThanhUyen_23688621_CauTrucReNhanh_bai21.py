# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 19:25:43 2024

@author: HP
"""

a=int(input('nhập số: '))
if 0<=a<=9:
    chữ=('Khong', 'Mot', 'Hai', 'Ba', 'Bon', 'Nam', 'Sau', 'Bay', 'Tam', 'Chin')
    print(chữ[a])
else:
    print('khong doc duoc')
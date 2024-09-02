# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 17:26:52 2024

@author: HP
"""

a=int(input('nhập giờ: '))
b=int(input('nhập phút: '))
c=int(input('nhập giây: '))
if 0<=a<=23 and 0<=b<=59 and  0<=c<=59:
    print(f'-->thời gian đã nhập: {a}giờ {b}phút {c}giây \n *kiểm tra tính hợp lệ của giờ, phút, giây:')
else:
    print('-->kiểm tra tính hợp lệ của giờ, phút, giây:')
if 0<=a<=23:
    print(f'-giờ hợp lệ: {a}giờ')
else:
    print('-giờ không hợp lệ')
if 0<=b<=59:
    print(f'-phút hợp lệ: {b}phút')
else:
    print('-phút không hợp lệ')
if 0<=c<=59:
    print(f'-giây hợp lệ: {c}giây')
else:
    print('-giây không hợp lệ')



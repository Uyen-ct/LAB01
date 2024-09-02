# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 19:36:55 2024

@author: HP
"""


a = input('Nhập thời gian theo định dạng hh:mm:ss: ')
gio, phut, giay = map(int, a.split(':'))
tong_giay = gio * 3600 + phut * 60 + giay
print(f'Tổng số giây: {tong_giay}')



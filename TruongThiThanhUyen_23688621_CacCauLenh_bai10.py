# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 14:45:37 2024

@author: HP
"""
SoXe_str = input('Nhập số xe của bạn( gồm 4 số): ')
def TongCacChuSo(SoXe_str):
    if len(SoXe_str) == 4 and SoXe_str.isdigit():
        tong = sum(int(ChuSo) for ChuSo in SoXe_str)
        return tong
    else:
        return 'không thể tính số nút\n ->Số xe phải có 4 chữ số'

kq = TongCacChuSo(SoXe_str)
print(f'Số nút của xe bạn: {kq}')


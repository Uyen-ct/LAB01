# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 16:16:33 2024

@author: HP
"""

N = input('Nhập N( gồm 2 số): ')
def TongCacChuSo(N):
    if len(N) == 2 and N.isdigit():
        tong = sum(int(ChuSo) for ChuSo in N)
        return tong
    else:
        return 'không thể tính\n ->Phải nhập số có 2 chữ số'

kq = TongCacChuSo(N)
print(f'Tổng các chữ số của N: {kq}')

# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 12:17:53 2024

@author: HP
"""
import math
a=input('Nhập hình(v,n,t): ')
if a=='v':
    print('Tính P và S của hình vuông')
    b=float(input('Nhập độ dài cạnh= '))
    P=b*4
    S=math.pow(b,2)
    print(f'\tKết quả P= {P}; S= {S}')
elif a=='n':
    print('Tính P và S của hình chữ nhật')
    b=float(input('Nhập chiều dài= '))
    c=float(input('Nhập chiều rộng= '))
    P=(b+c)*2
    S=b*c
    print(f'\tKết quả P= {P}; S= {S}')
elif a=='t':
    print('--Nhập bán kính chọn 1; Nhập đường kính chọn 2--')
    v=int(input('Mời chọn số: '))
    if v==1:
        print('Tính P và S của hình tròn')
        b=float(input('Nhập bán kính= '))
        P=b*2*3.14
        S=math.pow(b,2)*3.14
        print(f'\tKết quả P= {P}; S= {S}')
    elif v==2:
        print('Tính P và S của hình tròn')
        b=float(input('Nhập đường kính= '))
        P=b*3.14
        S=(math.pow(b,2)/4)*3.14
        print(f'\tKết quả P= {P}; S= {S}')
    else:
        print('Sai cú pháp\n--> chỉ chọn 1 hoặc 2')
else:
    print('Sai cú pháp\n--> chỉ chọn v hoặc n hoặc t')
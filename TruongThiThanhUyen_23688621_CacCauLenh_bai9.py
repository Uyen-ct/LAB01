# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 20:45:06 2024

@author: HP
"""

print('============ MENU ============')
print('1. Hu tieu \n2. Chao long\n3. Banh canh\n4. Bun rieu\n5. Pho bo ')
print('==============================')
a=int(input('Moi nhap lua chon:'))
print('==============================')
if a==1:
    print('Món bạn chọn: Hu tieu')
elif a==2:
    print('Món bạn chọn: Chao long')
elif a==3:
    print('Món bạn chọn: Banh canh')
elif a==4:
    print('Món bạn chọn: Bun rieu')
elif a==5:
    print('Món bạn chọn: Pho bo')
else:
    print('Chỉ chọn món từ 1 đến 5')

# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 18:55:21 2024

@author: HP
"""

a1=int(input('nhập giờ cho thời gian 1: '))
b1=int(input('nhập phút cho thời gian 1: '))
c1=int(input('nhập giây cho thời gian 1: '))

a2=int(input('nhập giờ cho thời gian 2: '))
b2=int(input('nhập phút cho thời gian 2: '))
c2=int(input('nhập giây cho thời gian 2: '))

a=a1+a2
b=b1+b2
c=c1+c2

d=abs(a1-a2)
e=abs(b1-b2)
f=abs(c1-c2)

print(f'Tổng hai giờ: {a}giờ, {b}phút, {c}giây\nHiệu hai giờ: {d}giờ, {e}phút, {f}giây')

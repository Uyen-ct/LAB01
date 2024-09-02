# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 20:02:13 2024

@author: HP
"""
import math
a=float(input('nhập a: '))
b=float(input('nhập b: '))
c=float(input('nhập c: '))
delta=math. pow(b,2)-(4*a*c)
if a!=0 and delta==0:
    print('phương trình có nghiệm kép x1=x2=',-b/(2*a))
elif a!=0 and delta>0:
    print('phương trình có 2 nghiệm phân biệt:')
    print('x1=',(-b+math.sqrt(delta))/2*a)
    print('x2=',(-b-math.sqrt(delta))/2*a)
elif a!=0 and delta<0:
    print('phương trình vô nghiệm')
else:
    print('không phải phương trình bậc 2')
    
    
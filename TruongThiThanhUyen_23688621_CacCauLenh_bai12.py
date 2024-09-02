# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 17:05:04 2024

@author: HP
"""

import random


so_nguyen_a = random.randint(0, 100)
so_thuc_a = random.uniform(0, 100)
so_nguyen_b = random.randint(50, 99)
so_thuc_b = random.uniform(50, 99)
so_nguyen_c = random.randint(-39, 79)
so_thuc_c = random.uniform(-39, 79)
so_nguyen_d = random.randint(-79, -39)
so_thuc_d = random.uniform(-79, -39)
print(f"Số nguyên ngẫu nhiên từ 0- 100: \t{so_nguyen_a}")
print(f"Số nguyên ngẫu nhiên từ 50- 99: \t{so_nguyen_b}")
print(f"Số nguyên ngẫu nhiên từ -39 đến 79: \t{so_nguyen_c}")
print(f"Số nguyên ngẫu nhiên từ -79 đến -39: \t{so_nguyen_d}")
print('')
print(f"Số thực ngẫu nhiên từ 0- 100: \t{so_thuc_a}")
print(f"Số thực ngẫu nhiên từ 50- 99: \t{so_thuc_b}")
print(f"Số thực ngẫu nhiên từ -39 đến 79: \t{so_thuc_c}")
print(f"Số thực ngẫu nhiên từ -79 đến -39: \t{so_thuc_d}")
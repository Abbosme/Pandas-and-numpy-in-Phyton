# -*- coding: utf-8 -*-
"""Untitled4.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1RIsR09NVaOixlSgxId-R_7gYCxgJMnAQ
"""

import numpy as np

#1. Massiv yaratish
# Bu Abbos ishi
array_1d = np.array([1, 2, 3, 4, 5])
array_2d = np.array([[1, 2, 3,], [4, 5, 6 ]])

#2. Matematik operatsalar
sum_array = np.sum(array_1d)
mean_array = np.mean(array_1d)
product_array = np.prod(array_1d)

print("1D Massiv:", array_1d)
print("2D Massiv:\n", array_2d)
print("Massiv yig'indisi:", sum_array)
print("O'rtacha:", mean_array)
print("Ko'paytmasi:", product_array)
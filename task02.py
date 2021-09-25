'''Посчитать коэффициент линейной регрессии при заработной плате (zp),
используя градиентный спуск (без intercept)'''

import numpy as np

x = np.array([35, 45, 190, 200, 40, 70, 54, 150, 120, 110])
y = np.array([401, 574, 874, 919, 459, 739, 653, 902, 746, 832])
n = len(x)

def mse(b1, y=y, x=x, n=len(x)):
    return np.sum((b1 * x - y) ** 2) / n


b1 = 0.1
alpha = 1e-6
for i in range(1000):
    b1 -= alpha * (2 / n) * np.sum((b1 * x - y) * x)
    if i % 100 == 0:
        print(f'iteration {i}: b1 = {b1}, mse = {mse(b1)}')

# получаем B = 5.8898 между 400 и 500 итерациями в модели без интерсепта


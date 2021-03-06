'''Даны значения величины заработной платы заемщиков банка (zp)
и значения их поведенческого кредитного скоринга (ks):
zp = [35, 45, 190, 200, 40, 70, 54, 150, 120, 110],
ks = [401, 574, 874, 919, 459, 739, 653, 902, 746, 832].
Используя математические операции, посчитать коэффициенты линейной регрессии,
приняв за X заработную плату (то есть, zp - признак),
а за y - значения скорингового балла (то есть, ks - целевая переменная).
Произвести расчет как с использованием intercept, так и без'''

import numpy as np

# Найдем коэффициенты уравнения y=a+bx
x = np.array([35, 45, 190, 200, 40, 70, 54, 150, 120, 110])
y = np.array([401, 574, 874, 919, 459, 739, 653, 902, 746, 832])
n = len(x)
b = (np.mean(y * x) - np.mean(x) * np.mean(y)) / (np.mean(x ** 2) - np.mean(x) ** 2)
print(b)  # b = 2.62
a = np.mean(y) - b * np.mean(x)
print(a)  # a = 444.18 (интерсепт)
r = b * np.std(x, ddof=1) / np.std(y, ddof=1)
print(r, r ** 2)  # коэф корреляции 0.8875 (результат сходится с решением из предыдущего занятия)
                  # 78,8% значений изменчивoсти признака оценивает полученная модель
X = x.reshape(10, 1)
Y = y.reshape(10, 1)
B = np.dot(np.linalg.inv(np.dot(X.T, X)), X.T @ Y)
print(B) # 5.8898 без интерсепта
X = np.hstack([np.ones((10,1)), X])
B = np.dot(np.linalg.inv(np.dot(X.T, X)), X.T @ Y)
print(B) # интерсепт 444.17, b = 2.62

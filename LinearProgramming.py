import numpy as np
from scipy.optimize import linprog
import matplotlib.pyplot as plt

# Заданная информация
a1 = 19
a2 = 16
a3 = 19
b1 = 31
b2 = 9
b3 = 1
c1 = 1121
c2 = 706
c3 = 1066
alpha = 16
beta = 19

# Формирование коэффициентов целевой функции и ограничений
c = [-alpha, -beta]  # Минимизируемая целевая функция
A = np.vstack([[a1, b1], [a2, b2], [a3, b3]])
b = [c1, c2, c3]

# Решение задачи линейного программирования
res = linprog(c, A_ub=A, b_ub=b, method='highs')

# Вывод результатов
x = res.x
max_profit = -res.fun

print("Значение x1 =", x[0])
print("Значение x2 =", x[1])
print("Максимальная прибыль =", max_profit)

# Отрисовка графика
labels = ['A', 'B']
sizes = [x[0], x[1]]
colors = ['gold', 'yellowgreen']
explode = (0.1, 0)

plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
plt.axis('equal')
plt.show()
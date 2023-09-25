import pulp
import matplotlib.pyplot as plt

# Исходные данные для задачи 1
a1 = 14
a2 = 15
a3 = 20
b1 = 40
b2 = 27
b3 = 4
c1 = 1200
c2 = 993
c3 = 1097
alpha = 5
beta = 13

# Создание оптимизационной задачи
prob = pulp.LpProblem("MaximizeProfit", pulp.LpMaximize)

# Определение переменных решения
x = pulp.LpVariable("xA", lowBound=0)
y = pulp.LpVariable("xB", lowBound=0)

# Определение целевой функции
prob += alpha * x + beta * y

# Добавление ограничений на использование материалов
prob += a1 * x + b1 * y <= c1
prob += a2 * x + b2 * y <= c2
prob += a3 * x + b3 * y <= c3

# Решение задачи линейного программирования
prob.solve()

# Вывод результатов
print("Максимальная прибыль:", pulp.value(prob.objective))
print("Количество продукции A:", pulp.value(x))
print("Количество продукции B:", pulp.value(y))

# Построение векторного графика
fig, ax = plt.subplots()
ax.quiver(0, 0, pulp.value(x), pulp.value(y), angles='xy', scale_units='xy', scale=1, color='blue')
ax.set_xlim([0, max(pulp.value(x), pulp.value(y)) + 10])
ax.set_ylim([0, max(pulp.value(x), pulp.value(y)) + 10])
plt.xlabel("Product A")
plt.ylabel("Product B")
plt.title("Optimal Production")
plt.grid()
plt.show()

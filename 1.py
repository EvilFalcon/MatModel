import cvxpy as cp

# Данные
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

# Переменные
x = cp.Variable()
y = cp.Variable()

# Ограничения
constraints = [
    a1 * x + b1 * y <= c1,
    a2 * x + b2 * y <= c2,
    a3 * x + b3 * y <= c3,
    x >= 0,
    y >= 0
]

# Целевая функция
objective = cp.Maximize(alpha * x + beta * y)

# Создание задачи и ее решение
problem = cp.Problem(objective, constraints)
result = problem.solve(solver=cp.HIGHS)

# Вывод результатов
print("Максимальная прибыль: ", result)
print("Значение x: ", x.value)
print("Значение y: ", y.value)
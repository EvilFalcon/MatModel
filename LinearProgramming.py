import pulp
import matplotlib.pyplot as plt
"""
проверка проведена на задаче №1 которая была дана на паре 26,9

Компания «Краски для покраски» производит краску для
внутренних и наружных работ из сырья двух типов: М1 и М2. Следующая
таблица представляет основные данные для задачи.
Отдел маркетинга компании ограничил ежедневное производство
краски для внутренних работ до 2 тонн (из-за отсутствия надлежащего
спроса), а также поставил условие, чтобы ежедневное производство краски
для внутренних работ не превышало более чем на тонну аналогичный
показатель производства краски для внешних работ. Компания хочет
определить оптимальное (наилучшее) соотношение между видами
выпускаемой продукции для максимизации общего ежедневного дохода.


а1=6 ;а2=1 ;в1=4 ;в2=2 ;с1=24 ;с2=6 ;А=5 ;В=4 ;
Максимальная прибыль: 2.6666667
Количество продукции A: 2.6666667
Количество продукции B: 1.6666667
"""
# Исходные данные для задачи :
a1 = int(input("a1= "))
a2 = int(input("a2= "))
#a3 = int(input("a3= "))
b1 = int(input("b1= "))
b2 = int(input("b2= "))
#b3 =int(input("b3= "))
c1 = int(input("c1= "))
c2 = int(input("c2= "))
#c3 = int(input("c3= "))
alpha =int(input("alpha= "))
beta =int(input("beta= "))

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
#prob += a3 * x + b3 * y <= c3
prob += x,y >= 0
prob += x-y <= 1
prob += y <= 2

# Решение задачи линейного программирования
prob.solve()

# Вывод результатов
print("Максимальная прибыль:", pulp.value(prob.objective))
print("Количество продукции A:", pulp.value(x))
print("Количество продукции B:", pulp.value(y))


# Построение векторного графика
fig, ax = plt.subplots()
ax.quiver(0, 0, pulp.value(x), pulp.value(y), angles='xy', scale_units='xy', scale=1, color='blue')
ax.set_xlim([0, max(pulp.value(x),pulp.value(y)) + 15])
ax.set_ylim([0, max(pulp.value(x),pulp.value(y)) + 15])
plt.xlabel("Product A")
plt.ylabel("Product B")
plt.title("Optimal Production")
plt.grid()
plt.show()
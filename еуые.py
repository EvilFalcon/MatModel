import pulp
import matplotlib.pyplot as plt

a1 = int(input("a1= "))
a2 = int(input("a2= "))
b1 = int(input("b1= "))
b2 = int(input("b2= "))
c1 = int(input("c1= "))
c2 = int(input("c2= "))
alpha = int(input("alpha= "))
beta = int(input("beta= "))

prob = pulp.LpProblem("MaximizeProfit", pulp.LpMaximize)

x = pulp.LpVariable("xA", lowBound=0, cat='Integer')
y = pulp.LpVariable("xB", lowBound=0, cat='Integer')

prob += alpha * x + beta * y

prob += a1 * x + b1 * y <= c1
prob += a2 * x + b2 * y <= c2
prob += x, y >= 0
prob += x - y <= 1
prob += y <= 2

prob.solve()

print("Максимальная прибыль:", round(pulp.value(prob.objective)))
print("Количество продукции A:", round(pulp.value(x)))
print("Количество продукции B:", round(pulp.value(y)))

fig, ax = plt.subplots()
ax.quiver(0, 0, round(pulp.value(x)), round(pulp.value(y)), angles='xy', scale_units='xy', scale=1, color='blue')
ax.set_xlim([0, max(round(pulp.value(x)), round(pulp.value(y))) + 15])
ax.set_ylim([0, max(round(pulp.value(x)), round(pulp.value(y))) + 15])
plt.xlabel("Product A")
plt.ylabel("Product B")
plt.title("Optimal Production")
plt.grid()
plt.show()
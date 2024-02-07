#Tsygankov_HW10_1

from pulp import *

# Ініціалізація змінних
lemonade = LpVariable("Lemonade", lowBound=0, cat='Integer')
fruit_juice = LpVariable("Fruit_Juice", lowBound=0, cat='Integer')

# Ініціалізація проблеми максимізації
prob = LpProblem("Maximize_Products", LpMaximize)

# Функція максимізації
prob += lemonade + fruit_juice

# Обмеження ресурсів
prob += 2 * lemonade + fruit_juice <= 100  # Вода
prob += lemonade <= 50  # Цукор
prob += lemonade <= 30  # Лимонний сік
prob += 2 * fruit_juice <= 40  # Фруктове пюре

# Обмеження на кількість продуктів
prob += lemonade >= 0
prob += fruit_juice >= 0

# Вирішення проблеми
prob.solve()

# Виведення результатів
print("Status:", LpStatus[prob.status])
print("Maximum number of Lemonade:", value(lemonade))
print("Maximum number of Fruit Juice:", value(fruit_juice))
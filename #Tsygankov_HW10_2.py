#Tsygankov_HW10_2

import numpy as np
import scipy.integrate as spi
import matplotlib.pyplot as plt

# Визначення функції та межі інтегрування
def f(x):
    return x ** 2

def monte_carlo_integration(func, a, b, num_samples=10000):
    # Генерування випадкових точок
    x_samples = np.random.uniform(a, b, num_samples)
    y_samples = np.random.uniform(0, max(func(x_samples)), num_samples)
    
    # Обчислення кількості точок, які потрапили під криву
    points_under_curve = sum(y_samples <= func(x_samples))
    
    # Визначення площі прямокутника
    total_area = (b - a) * max(func(x_samples))
    
    # Обчислення інтеграла
    integral = total_area * (points_under_curve / num_samples)
    
    return integral

if __name__ == "__main__":
    a = 0  # Нижня межа
    b = 2  # Верхня межа

    # Обчислення інтеграла методом Монте-Карло
    monte_carlo_result = monte_carlo_integration(f, a, b)

    # Обчислення інтеграла за допомогою функції quad
    quad_result, _ = spi.quad(f, a, b)

    # Виведення результатів
    print("Інтеграл методом Монте-Карло:", monte_carlo_result)
    print("Інтеграл за допомогою quad:", quad_result)
    print("Різниця між Монте-Карло та quad:", abs(monte_carlo_result - quad_result))

    # Побудова графіка
    x = np.linspace(a, b, 400)
    y = f(x)

    plt.plot(x, y, 'r', linewidth=2)
    plt.fill_between(x, y, color='gray', alpha=0.3)
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.title('Метод Монте-Карло для обчислення інтеграла')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.grid()
    plt.show()


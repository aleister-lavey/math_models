import random
import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return np.cos(5 * x) * x ** 3

def df(x):
    return 3 * x ** 2 * np.cos(5 * x) - 5 * x ** 3 * np.sin(5 * x) 

y_min_global = 0
x_min = -3
x_max = 3
grad_iterations = 100
grad_cycles = 1000
grad_step = 100

for _ in range(grad_iterations):
    x = random.uniform(x_min,x_max)

    for i in range(grad_cycles):
        learning_rate = 1 / min( i + 10, grad_step)
        x = x - learning_rate * np.sign(df(x))
        if x < x_min - (x_min / 10)  or x > x_max - (x_max / 10):
            break
        else:
            y_min_local = f(x)
        if y_min_local < y_min_global:
            y_min_global = y_min_local

print(f'global minimum is: {y_min_global}')

x_plt = np.arange(x_min, x_max, 0.1)
f_plt = [f(x) for x in x_plt]
plt.ion()
fig, ax = plt.subplots()
ax.grid(True)
plt.ioff()
ax.plot(x_plt, f_plt)
plt.show()

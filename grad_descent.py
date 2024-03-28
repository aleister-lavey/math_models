import random
import matplotlib.pyplot as plt
import numpy as np


def f(x):
    return np.cos(5 * x) * x ** 3


def df(x):
    return x ** 2 * (1.5 * np.cos(5 * x) - 2.5 * x * np.sin(5 * x))


#learning_rate = 0.1
grad_iterations = 100
step_size = 100

print(".............GRADIENT......DESCENT.....................")
#x_min = float(input("Input minimal x:"))
#x_max = float(input("Input max x:"))
x = 0
x_max = 3
x_min = -3
y_min_global = f(x)
for _ in range(100):
    x = random.uniform(-3,3)
    
    for i in range(grad_iterations):
        learning_rate = 1 / min( i + 1, step_size)
        #learning_rate = 0.01
        x = x - learning_rate * np.sign(df(x))
    y_min_local = f(x)
if y_min_global > y_min_local:
     y_min_global = y_min_local
    
print(f"Minimal function value on segment ({x_min};{x_max}):","x=", round(x,3),"y=", round(y_min_global,3))

x_plt = np.arange(x_min, x_max, 0.1)
f_plt = [f(x) for x in x_plt]

plt.ion()
fig, ax = plt.subplots()
ax.grid(True)
plt.ioff()
ax.plot(x_plt, f_plt)
plt.show()

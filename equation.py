import numpy as np
import random
import matplotlib.pyplot as plt

def f(x):
    return (np.sin(x) * np.cos(x) + np.log(x ** 2)) / (x ** 2)
    
a = -2
b = -1
c = (a + b) / 2

x_left = a
x_right = b
eps = 0.0001

# метод бисекции
while x_left - x_right > eps:
    cent = (x_right - x_left) / 2
    x_i = x_left + cent
    if np.sign(f(x_left)) != np.sign(f(x_i)):
        x_right = x_i
    else:
        x_left = x_i
print(f'x_i ={x_i}')
# конец метода бисекции

x_plt = np.arange(a, b, 0.001)
f_plt = [f(x) for x in x_plt]

fig, ax = plt.subplots()
ax.grid(True)

ax.plot(x_plt, f_plt)
plt.show()

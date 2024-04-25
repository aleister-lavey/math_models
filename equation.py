import numpy as np
import random
import matplotlib.pyplot as plt
def f(x):
    return (np.sin(x) * np.cos(x) + np.log(x ** 2)) / (x ** 2)

# interval [a,b]
a = -2
b = -1

x_plt = np.arange(a, b, 0.001)
f_plt = [f(x) for x in x_plt]

fig, ax = plt.subplots()
ax.grid(True)

ax.plot(x_plt, f_plt)
plt.show()

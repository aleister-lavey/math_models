import numpy as np
import random
import matplotlib.pyplot as plt

def f(x):
    return (np.sin(x) * np.cos(x) + np.log(x ** 2)) / (x ** 2)
    
a = -2
b = -1
c = (a + b) / 2

#left_interval = np.arange(a , c , 0.001)
#right_interval = np.arange(c , b , 0.001)

#for i in left_interval:
#    if np.sign(f(i)) != np.sign(f(i - 0.001)):
#        print('found root')

x_plt = np.arange(a, b, 0.001)
f_plt = [f(x) for x in x_plt]

fig, ax = plt.subplots()
ax.grid(True)

ax.plot(x_plt, f_plt)
plt.show()

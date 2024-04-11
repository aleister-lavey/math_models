import numpy as np
import random

#first example function
def f(x):
    return (x + np.cos(x)) / (x ** 2 + 2 * np.sin(x))

# interval [a,b]
a = 1
b = 3 ** 0.5

N = 1000000

#rectangle method
rectangle_width = (b - a) / N

#right rectangle area method

area_right = 0

for i in range(N):
    area_right += rectangle_width * f(a + rectangle_width * i)
print(f'rigth rectangle method area = {area_right}')

#left rectangle area method

area_left = 0

for i in range(1,N):
    area_left += rectangle_width * f(a + rectangle_width * i - rectangle_width)
print(f'left rectangle method area  = {area_left}')

area_trap = 0

#trapezoid method

j = 1
for i in range(N):
    area_trap += rectangle_width * ( (f(a + i * rectangle_width) + f(a + j * rectangle_width)) / 2)
    j += 1
print(f'trapezoid method area       = {area_trap}')

#Monte - Carlo
area_carlo = 0

for i in range(N):
    gen = random.random() * (b - a) + a
    area_carlo += f(gen) * rectangle_width
    
print(f'monte_carlo method area     = {area_carlo}')

# Homer Simpson method

area_simpson_first = rectangle_width / 3 * f(a)
area_simpson_even = 0 
area_simpson_odd = 0
area_simpson_last = rectangle_width / 3 * f(b)

even = []
odd = []

for i in range(1 , N):
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)

for i in range(len(even)):
    area_simpson_even += 2 / 3 * rectangle_width * f(even[i] * rectangle_width + a)

for i in range(len(odd)):
    area_simpson_odd += 4 / 3 * rectangle_width * f(odd[i] * rectangle_width + a)
print(f'homer simpson method area   = {(area_simpson_first + area_simpson_even + area_simpson_odd + area_simpson_last)}')

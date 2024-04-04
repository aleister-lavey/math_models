import numpy as np
import random

#first example function
def f(x):
    return np.sin(x)

# interval [a,b]
a = 0
b = np.pi

N = int(input("input approximity number: "))


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
print(f'left rectangle method area = {area_left}')

area_trap = 0

#trapezoid method

j = 1
for i in range(N):
    area_trap += rectangle_width * ( (f(a + i * rectangle_width) + f(a + j * rectangle_width)) / 2)
    j += 1
print(f'trapezoid method area = {area_trap}')



#Monte - Carlo
area_carlo = 0


for i in range(N):
    gen = random.random() * (b - a) + a
    area_carlo += f(gen) * rectangle_width
    
print(f'monte_carlo method area = {area_carlo}')

# Homer Simpson method

h = (b - a) / (N * 2)

area_simpson1 =  (h / 3) * f(a)
area_simpson2 = 0
area_simpson3 = 0
area_simpson4 = (h / 3) * f(b)

even = []
odd = []

for i in range(N):
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)

for i in range(len(even)):
    area_simpson2 += (h / 3) * (2 * (f(even[i] * h)))
    
for i in range(len(odd)):
    area_simpson3 += (h / 3) * (4 * (f(odd[i] * h)))
    
print(f'homer simpson method area = {2 * (area_simpson1 + area_simpson2 + area_simpson3 + area_simpson4)}')

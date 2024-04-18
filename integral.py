import numpy as np
import random

def f(x):
    return np.e ** x * np.cos(x)

true_area = (np.e) ** (np.pi / 2) / 2 - 0.5

N = int(random.uniform(1,10000))
print(N)

print(f'original integral value     =          {true_area}\n')

# interval [a,b]
a = 0
b = np.pi / 2

errors = []
rectangle_width = (b - a) / N

#right rectangle area method
area_right = 0
for i in range(N):
    area_right += rectangle_width * f(a + rectangle_width * i)
right_rectangle_relative_error = (true_area - area_right) / true_area
errors.append(right_rectangle_relative_error)

print(f'rigth rectangle method area =          {area_right}')
print(f'rigth rectangle method absolute error: {true_area - area_right}')
print(f'rigth rectangle method relative error: {right_rectangle_relative_error}\n')

#left rectangle area method
area_left = 0
for i in range(1,N):
    area_left += rectangle_width * f(a + rectangle_width * i - rectangle_width)
left_rectangle_relative_error = (true_area - area_left) / true_area
errors.append(left_rectangle_relative_error)    

print(f'left rectangle method area  =          {area_left}')
print(f'left rectangle method absolute error:  {true_area - area_left}')
print(f'left rectangle method relative error:  {left_rectangle_relative_error}\n')

#trapezoid method
area_trap = 0
j = 1
for i in range(N):
    area_trap += rectangle_width * ( (f(a + i * rectangle_width) + f(a + j * rectangle_width)) / 2)
    j += 1
trap_relative_error = (true_area - area_trap) / true_area
errors.append(trap_relative_error) 

print(f'trapezoid method area       =          {area_trap}')
print(f'trapezoid method absolute error:       {true_area - area_trap}')
print(f'trapezoid method relative error:       {trap_relative_error}\n')

#Monte - Carlo
area_carlo = 0
for i in range(N):
    gen = random.random() * (b - a) + a
    area_carlo += f(gen) * rectangle_width
monte_carlo_relative_error = (true_area - area_carlo) / true_area
errors.append(monte_carlo_relative_error) 

print(f'monte_carlo method area     =          {area_carlo}')
print(f'monte_carlo method absolute error:     {true_area - area_carlo}')
print(f'monte_carlo method relative error:     {monte_carlo_relative_error}\n')

# THE MIGHTY HOMER SIMPSON METHOD BY BRATASH PAVEL
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
area_simpson = area_simpson_first + area_simpson_even + area_simpson_odd + area_simpson_last
homer_simpson_relative_error = (true_area - area_simpson) / true_area
errors.append(homer_simpson_relative_error)

print(f'homer simpson method area   =          {(area_simpson)}')
print(f'homer simpson method absolute error:   {true_area - area_simpson}')
print(f'homer simpson method relative error:   {homer_simpson_relative_error}\n')

############################################################################################
############################################################################################
# What's the best method?

for i in range(len(errors)):
    if errors[i] < 0:
        errors[i] = errors[i] * (-1)
        errors_min = min(errors)
        
if errors.index(errors_min) == 0:
    print('right rectangle is the best!')
if errors.index(errors_min) == 1:
    print('left rectangle is the best!')
if errors.index(errors_min) == 2:
    print('trapezoid is the best!')
if errors.index(errors_min) == 3:
    print('monte_carlo is the best!')
if errors.index(errors_min) == 4:
    print('HOMER SIMPSON IS THE BEST!')

import numpy as np

#first example function
def f(x):
    return (x ** 5 + np.sin(x) + np.tan(x / 2)) / (np.sin(37 * x))

# interval [a,b]
a = 2
b = 4
S1 = 0

N = int(input("input approximity number: "))


#rectangle method
rectangle_width = (b - a) / N



for i in range(N):
    S1 += rectangle_width * f(a + rectangle_width * i)
print(f'rectangle method area = {S1}')

S2 = 0
#trapezoid method
j = 1
for i in range(N):
    S2 += rectangle_width * ( (f(a + i * rectangle_width) + f(a + j * rectangle_width)) / 2)
    j += 1
print(f'trapezoid method area = {S2}')

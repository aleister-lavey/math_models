# Мат. и комп. моделирование #
## 1 Лаба - Grad_descent ##
Градиентный спуск для любой дифференцируемой функции, заданной на отрезке. Заранее вбить в методы саму функцию и ее производную.
## 2 Лаба - Gamblers_ruin - задача о разорении игрока ##
За столом сидят два игрока. У первого в распоряжении находится x рублей, у второго в распоряжении находится y рублей.
Перед ними на столе лежит ассиметричная монета(вероятность того, что выпадет орел, равняется p).
Если на монете выпадает орел, то рубль выигрывает первый игрок (второй игрок выплачивает первому 1 рубль), а если выпадает решка, то первый игрок платит второму рубль.
Максимальное количество шагов - N, число игр N_game. Требуется найти вероятность проигрыша каждого игрока и вычислить среднюю длину игры.
> Вводные данные:
> x0 = 111; y0 = 169; p = 0.52; N = 1000; N_game = 1000
## 3 Лаба - Integral - задача о вычислении определенного интеграла ##
Пусть дана фунция, определенная на интервале [a,b]. Необходимо найти площадь под кривой функции:
1) Методом левых прямоугольников 
2) Методом правых прямоугольников 
3) Методом трапеций
4) Методом Монте-Карло
5) Методом Симпсона 
## 4 Лаба - Equation - решение уравнений численными методами - методом бисекции и методом хорд ##
Дана функция f(x) = (np.sin(x) * np.cos(x) + np.log(x ** 2)) / (x ** 2). Δf(x) = 1e-12. Решить уравнение f(x) = 0 методом бисекций и методом хорд.

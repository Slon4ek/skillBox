# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1000, 1000)
t_point = sd.get_point(150, 150)
s_point = sd.get_point(150, 450)
p_point = sd.get_point(600, 600)
h_point = sd.get_point(600, 300)


# Часть 1.
# Написать функции рисования равносторонних геометрических фигур:
# - треугольника
# - квадрата
# - пятиугольника
# - шестиугольника
# Все функции должны принимать 3 параметра:
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Использование копи-пасты - обязательно! Даже тем кто уже знает про её пагубность. Для тренировки.
# Как работает копипаста:
#   - одну функцию написали,
#   - копипастим её, меняем название, чуть подправляем код,
#   - копипастим её, меняем название, чуть подправляем код,
#   - и так далее.
# В итоге должен получиться ПОЧТИ одинаковый код в каждой функции

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# sd.line()
# Результат решения см lesson_004/results/exercise_01_shapes.jpg


def figure_draw(point, side, length, angle):
    s_angle = 360 / side
    point_0 = point
    side -= 1
    for _ in range(side):
        v = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
        v.draw()
        point = v.end_point
        angle += s_angle
        sd.sleep(0.1)
    sd.line(start_point=v.end_point, end_point=point_0, width=3)


def triangle(point, angle=0, length=100):
    figure_draw(point, side=3, length=length, angle=angle)


def square(point, angle=0, length=100):
    figure_draw(point, side=4, length=length, angle=angle)


def pentagon(point, angle=0, length=100):
    figure_draw(point, side=5, length=length, angle=angle)


def hexagon(point, angle=0, length=100):
    figure_draw(point, side=6, length=length, angle=angle)


triangle(point=t_point, angle=10, length=200)
square(point=s_point, angle=30, length=200)
pentagon(point=p_point, angle=-30)
hexagon(point=h_point, angle=-60)
# Часть 1-бис.
# Попробуйте прикинуть обьем работы, если нужно будет внести изменения в этот код.
# Скажем, связывать точки не линиями, а дугами. Или двойными линиями. Или рисовать круги в угловых точках. Или...
# А если таких функций не 4, а 44?

# Часть 2 (делается после зачета первой части)
#
# Надо сформировать функцию, параметризированную в местах где была "небольшая правка".
# Это называется "Выделить общую часть алгоритма в отдельную функцию"
# Потом надо изменить функции рисования конкретных фигур - вызывать общую функцию вместо "почти" одинакового кода.
#
# В итоге должно получиться:
#   - одна общая функция со множеством параметров,
#   - все функции отрисовки треугольника/квадрата/етс берут 3 параметра и внутри себя ВЫЗЫВАЮТ общую функцию.
#
# Не забудте в этой общей функции придумать, как устранить разрыв
#   в начальной/конечной точках рисуемой фигуры (если он есть)

# Часть 2-бис.
# А теперь - сколько надо работы что бы внести изменения в код? Выгода на лицо :)
# Поэтому среди программистов есть принцип D.R.Y. https://clck.ru/GEsA9
# Будьте ленивыми, не используйте копи-пасту!


sd.pause()

# -*- coding: utf-8 -*-
from pprint import pprint

import simple_draw as sd

# Добавить цвет в функции рисования геом. фигур. из упр lesson_004/01_shapes.py
# (код функций скопировать сюда и изменить)
# Запросить у пользователя цвет фигуры посредством выбора из существующих:
#   вывести список всех цветов с номерами и ждать ввода номера желаемого цвета.
# Потом нарисовать все фигуры этим цветом

# Пригодятся функции
# sd.get_point()
# sd.line()
# sd.get_vector()
# и константы COLOR_RED, COLOR_ORANGE, COLOR_YELLOW, COLOR_GREEN, COLOR_CYAN, COLOR_BLUE, COLOR_PURPLE
# Результат решения см lesson_004/results/exercise_02_global_color.jpg

colors = {
    1: ('RED', sd.COLOR_RED),
    2: ('ORANGE', sd.COLOR_ORANGE),
    3: ('YELLOW', sd.COLOR_YELLOW),
    4: ('GREEN', sd.COLOR_GREEN),
    5: ('CYAN', sd.COLOR_CYAN),
    6: ('BLUE', sd.COLOR_BLUE),
    7: ('PURPLE', sd.COLOR_PURPLE)
}


def figure_draw(point, side, length, angle, color):
    s_angle = 360 / side
    point_0 = point
    side -= 1
    for _ in range(side):
        v = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
        v.draw(color=color)
        point = v.end_point
        angle += s_angle
        sd.sleep(0.1)
    sd.line(start_point=v.end_point, end_point=point_0, width=3, color=color)


def triangle(point, angle=0, length=100, color=sd.COLOR_ORANGE):
    figure_draw(point, side=3, length=length, angle=angle, color=color)


def square(point, angle=0, length=100, color=sd.COLOR_ORANGE):
    figure_draw(point, side=4, length=length, angle=angle, color=color)


def pentagon(point, angle=0, length=100, color=sd.COLOR_ORANGE):
    figure_draw(point, side=5, length=length, angle=angle, color=color)


def hexagon(point, angle=0, length=100, color=sd.COLOR_ORANGE):
    figure_draw(point, side=6, length=length, angle=angle, color=color)


print('Возможные цвета:')
for num, name in colors.items():
    print('    ', num, ':', name[0].lower())

while True:
    color = input('Укажите номер цвета: ')
    if color.isdigit():
        color = int(color)
        if color in colors:
            point = sd.get_point(400, 400)
            triangle(point=point, angle=20, length=100, color=colors[color][1])

            point = sd.get_point(100, 400)
            square(point=point, angle=20, length=100, color=colors[color][1])

            point = sd.get_point(400, 100)
            pentagon(point=point, angle=20, length=100, color=colors[color][1])

            point = sd.get_point(100, 100)
            hexagon(point=point, angle=20, length=100, color=colors[color][1])
            break
        else:
            print('Ошибка!: Неверно указан номер цвета.')
    else:
        print('Ошибка!: Указана буква.')
sd.pause()

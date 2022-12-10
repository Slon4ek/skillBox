# -*- coding: utf-8 -*-

import simple_draw as sd
sd.resolution = (1000, 1000)
sd.background_color = (255, 255, 255)
# Запросить у пользователя желаемую фигуру посредством выбора из существующих
#   вывести список всех фигур с номерами и ждать ввода номера желаемой фигуры.
# и нарисовать эту фигуру в центре экрана

# Код функций из упр lesson_004/02_global_color.py скопировать сюда
# Результат решения см lesson_004/results/exercise_03_shape_select.jpg

t_point = sd.get_point(150, 150)
s_point = sd.get_point(150, 450)
p_point = sd.get_point(600, 700)
h_point = sd.get_point(600, 300)


colors = {
    1: ('RED', sd.COLOR_RED),
    2: ('ORANGE', sd.COLOR_ORANGE),
    3: ('YELLOW', sd.COLOR_YELLOW),
    4: ('GREEN', sd.COLOR_GREEN),
    5: ('CYAN', sd.COLOR_CYAN),
    6: ('BLUE', sd.COLOR_BLUE),
    7: ('PURPLE', sd.COLOR_PURPLE)
}
figures = {
    1: 'Треугольник',
    2: 'Квадрат',
    3: 'Пятиугольник',
    4: 'Шестиугольник'
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


def triangle(point, angle=0, length=100, color=sd.COLOR_BLACK):
    figure_draw(point, side=3, length=length, angle=angle, color=color)


def square(point, angle=0, length=100, color=sd.COLOR_BLACK):
    figure_draw(point, side=4, length=length, angle=angle, color=color)


def pentagon(point, angle=0, length=100, color=sd.COLOR_BLACK):
    figure_draw(point, side=5, length=length, angle=angle, color=color)


def hexagon(point, angle=0, length=100, color=sd.COLOR_BLACK):
    figure_draw(point, side=6, length=length, angle=angle, color=color)


def color_choice():
    print('Возможные цвета:')
    for num, name in colors.items():
        print('    ', num, ':', name[0].lower())
    while True:
        color = input('Укажите номер цвета: ')
        if color.isdigit():
            color = int(color)
            if color in colors:
                return colors[color][1]
                break
            else:
                print('Ошибка!: Неверно указан номер цвета.')
        else:
            print('Ошибка!: Указана буква.')


print('Возможные фигуры: ')
for num, name in figures.items():
    print(f'      {num} : {name}')
while True:
    figure = input("Введите номер фигуры: ")
    if figure.isdigit():
        figure = int(figure)
        if figure in figures:
            color = color_choice()
            if figure == 1:
                triangle(point=t_point, color=color)
            elif figure == 2:
                square(point=s_point, color=color)
            elif figure == 3:
                pentagon(point=p_point, color=color)
            elif figure == 4:
                hexagon(point=h_point, color=color)
            break
        else:
            print('Такого номера нет в списке :( попробуйте еще раз.')
    else:
        print('Вы ввели букву/символ :( попробуйте еще раз.')
sd.pause()

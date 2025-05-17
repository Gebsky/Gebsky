# star.py

import turtle

def draw_nine_pointed_star(size=200):
    """
    Рисует девятиконечную звезду с заданным размером.

    Args:
        size (int): длина стороны звезды.
    """
    # Создаем экран и черепаху
    screen = turtle.Screen()
    star = turtle.Turtle()

    # Настраиваем скорость
    star.speed(10)

    # Количество линий и угол поворота
    num_points = 9
    angle = 160

    for _ in range(num_points):
        star.forward(size)
        star.right(angle)

    # Останавливаться, пока пользователь не закроет окно
    turtle.done()
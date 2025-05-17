## Hi there 👋
# Девятиконечная звезда с помощью turtle

Этот скрипт рисует девятиконечную звезду, используя модуль `turtle` в Python.

## Как запустить

1. Склонируйте репозиторий или скачайте файлы.
2. Убедитесь, что у вас установлен Python 3.
3. Запустите скрипт:

```bash
python star.pyimport turtle

def draw_nine_pointed_star():
    # Создаем экран и черепаху
    screen = turtle.Screen()
    star = turtle.Turtle()

    # Настраиваем скорость
    star.speed(10)

    # Количество линий и угол поворота
    num_points = 9
    angle = 160

    # Рисуем звезду
    for _ in range(num_points):
        star.forward(200)
        star.right(angle)

    # Завершаем
    turtle.done()

if __name__ == "__main__":
    draw_nine_pointed_star()
<!--

import sys
import turtle as t
from random import randint
from time import sleep


# field settings (настройки поля)
cell = 50
# количество ячеек по ширине
width = 16
# количество ячеек по длине
length = 12

window = t.Screen()
window.setup(cell * width + 120, cell * length + 120)


# window._root.resizable(False, False)
window.bgcolor('black')
window.title('CODDY snake')
window.tracer(0)


# строится сетка на поле
# grid - сетка
grid = t.Turtle()
grid.color('white')
grid.speed(0)
grid.penup()
grid.goto(-0.5 * cell * width, 0.5 * cell * length)



for i in range(0, width + 1):
    grid.pendown()
    if i % 2 == 0:
        directionx = -1
    elif i % 2 == 1:
        directionx = 1

    grid.sety(0.5 * cell * length * directionx)
    grid.penup()
    grid.forward(cell)


grid.penup()
grid.goto(-0.5 * cell * width, 0.5 * cell * length)





for i in range(0, length + 1):
    grid.pendown()
    if i % 2 == 0:
        grid.forward(cell * width)
    elif i % 2 == 1:
        grid.backward(cell * width)

    grid.penup()
    grid.sety(grid.pos()[1] - cell)
grid.hideturtle()

# spawn an apple
apple = t.Turtle()
apple.color('red')
apple.shape('square')
apple.shapesize(2)
apple.penup()
apple.hideturtle()

def spawn_apple(snake):

    while True:
        counter = 0
        x = randint(-int(width / 2 - 1), int(width / 2 - 1))
        y = randint(-int(length / 2 - 1), int(length / 2 - 1))

        x_apple = x * cell + cell / 2
        y_apple = y * cell + cell / 2

        for i in snake:
            if (x_apple == i.pos()[0] and y_apple == i.pos()[1]):
                counter += 1
                break
        if counter == 0:
            break

    apple.goto(x_apple, y_apple)
    apple.showturtle()





# создаем список-змейку
snake_head = t.Turtle()
snake_body1 = t.Turtle()
snake_body2 = t.Turtle()
snake_body3 = t.Turtle()

snake_head.color('green')
snake_body1.color('green')
snake_body2.color('green')
snake_body3.color('green')

snake_head.shape('square')
snake_body1.shape('square')
snake_body2.shape('square')
snake_body3.shape('square')

snake_head.shapesize(2)
snake_body1.shapesize(2)
snake_body2.shapesize(2)
snake_body3.shapesize(2)

snake_head.penup()
snake_body1.penup()
snake_body2.penup()
snake_body3.penup()

snake_head.sety(-cell / 2)
snake_body1.sety(-cell / 2)
snake_body2.sety(-cell / 2)
snake_body3.sety(-cell / 2)

snake_head.setx(-cell * 1.5)
snake_body1.setx(-cell * 0.5)
snake_body2.setx(cell * 0.5)
snake_body3.setx(cell * 1.5)

snake = [snake_head, snake_body1, snake_body2, snake_body3]


snakex = -1
snakey = 0


spawn_apple(snake)


def go_up():
    global snakex, snakey
    if snakey != -1:
        snakex = 0
        snakey = 1

def go_down():
    global snakex, snakey
    if snakey != 1:
        snakex = 0
        snakey = -1

def go_right():
    global snakex, snakey
    if snakex != -1:
        snakex = 1
        snakey = 0

def go_left():
    global snakex, snakey
    if snakex != 1:
        snakex = -1
        snakey = 0

t.onkey(go_up, 'Up')
t.onkey(go_down, 'Down')
t.onkey(go_right, 'Right')
t.onkey(go_left, 'Left')


def add_block():
    """increase the length of the snake"""
    block = t.Turtle()
    block.shape('square')
    block.color('green')
    block.shapesize(2)
    block.hideturtle()
    block.penup()

    return block


window.update()
window.tracer(1)

while True:

    # создаем список координат каждого блока змейки (предыдущие координаты)
    coords = []
    for i in snake:
        coords.append(i.pos())


    if ((snake_head.pos()[0] + cell * snakex) - (cell / 2)) < -(width / 2) * cell:
        sys.exit()

    if ((snake_head.pos()[0] + cell * snakex) + (cell / 2)) > (width / 2) * cell:
        sys.exit()


    if ((snake_head.pos()[1] + cell * snakey) + (cell / 2)) > (length / 2) * cell:
        sys.exit()


    if ((snake_head.pos()[1] + cell * snakey) - (cell / 2)) < -(length / 2) * cell:
        sys.exit()

    snake_head.setpos(snake_head.pos()[0] + cell * snakex, snake_head.pos()[1] + cell * snakey)





    for index, part in enumerate(snake[1:]):
        part.goto(coords[index])





    if (snake[0].pos()[0] == apple.pos()[0]) and (snake[0].pos()[1] == apple.pos()[1]):
        apple.hideturtle()

        if snake[-1].pos()[1] == snake[-2].pos()[1]:
            # змейка движется вправо
            if snakex == 1:
                snake_part = add_block()
                snake_part.setpos(snake[-1].pos()[0] - cell, snake[-1].pos()[1])
                snake_part.showturtle()
                snake.append(snake_part)

            # змейка движется влево
            elif snakex == -1:
                snake_part = add_block()
                snake_part.setpos(snake[-1].pos()[0] + cell, snake[-1].pos()[1])
                snake_part.showturtle()
                snake.append(snake_part)

        if snake[-1].pos()[0] == snake[-2].pos()[0]:
            # змейка движется вверх
            if snakey == 1:
                snake_part = add_block()
                snake_part.setpos(snake[-1].pos()[0], snake[-1].pos()[1] - cell)
                snake_part.showturtle()
                snake.append(snake_part)
            # змейка движется вниз
            elif snakey == -1:
                snake_part = add_block()
                snake_part.setpos(snake[-1].pos()[0], snake[-1].pos()[1] + cell)
                snake_part.showturtle()
                snake.append(snake_part)


        if (snake[0].pos()[1] == 1) and (snake[-2].pos()[1] == snake[-1].pos()[1]):

            if snake[-1].pos()[0] < snake[-2].pos()[0]:
                snake_part = add_block()
                snake_part.setpos(snake[-1].pos()[0] - cell, snake[-1].pos()[1])
                snake_part.showturtle()
                snake.append(snake_part)
            elif snake[-1].pos()[0] > snake[-2].pos()[0]:
                snake_part = add_block()
                snake_part.setpos(snake[-1].pos()[0] + cell, snake[-1].pos()[1])
                snake_part.showturtle()
                snake.append(snake_part)


        if ((snake[0].pos()[0] == -1) or (snake[0].pos()[0] == 1))  and (snake[-2].pos()[0] == snake[-1].pos()[0]):
            snake_part = add_block()
            snake_part.setpos(snake[-1].pos()[0], snake[-1].pos()[1] + cell)
            snake_part.showturtle()
            snake.append(snake_part)


        if (snake[0].pos()[1] == -1) and (snake[-2].pos()[1] == snake[-1].pos()[1]):

            if snake[-1].pos()[0] < snake[-2].pos()[0]:
                snake_part = add_block()
                snake_part.setpos(snake[-1].pos()[0] - cell, snake[-1].pos()[1])
                snake_part.showturtle()
                snake.append(snake_part)
            elif snake[-1].pos()[0] > snake[-2].pos()[0]:
                snake_part = add_block()
                snake_part.setpos(snake[-1].pos()[0] + cell, snake[-1].pos()[1])
                snake_part.showturtle()
                snake.append(snake_part)

        spawn_apple(snake)









    t.listen()
    sleep(0.15)

t.mainloop()






















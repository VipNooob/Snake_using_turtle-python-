import turtle as t
from random import randint
from copy import deepcopy
from time import sleep
# field settings (настройки поля)
cell = 50
# количество ячеек по ширине
width = 16
# количество ячеек по длине
length = 12

window = t.Screen()
window.setup(cell * width + 2, cell * length + 2)

window._root.resizable(False, False)
window.bgcolor('black')
window.title('CODDY snake')

# строится сетка на поле
# grid - сетка
grid = t.Turtle()
grid.color('white')
grid.speed(0)
grid.penup()
grid.goto(-0.5 * cell * width + cell, 0.5 * cell * length)
grid.pendown()


for i in range(0, width - 1):
    if i % 2 == 0:
        directionx = -1
    elif i % 2 == 1:
        directionx = 1

    grid.sety(cell * length * directionx)
    grid.forward(cell)


grid.penup()
grid.goto(-0.5 * cell * width, 0.5 * cell * length - cell)
grid.pendown()

for i in range(0, length - 1):
    if i % 2 == 0:
        grid.forward(cell * width)

    elif i % 2 == 1:
        grid.backward(cell * width)

    grid.sety(grid.pos()[1] - cell)

# spawn an apple
apple = t.Turtle()
apple.color('red')
apple.shape('square')
apple.shapesize(2)
apple.penup()
apple.hideturtle()
apple.goto(randint(-int(width / 2 - 1), int(width / 2 - 1)) * cell + cell / 2, randint(-int(length / 2 - 1), int(length / 2 - 1)) * cell + cell / 2)
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

def go_up():
    global snakex, snakey
    snakex = 0
    snakey = 1

def go_down():
    global snakex, snakey
    snakex = 0
    snakey = -1

def go_right():
    global snakex, snakey
    snakex = 1
    snakey = 0

def go_left():
    global snakex, snakey
    snakex = -1
    snakey = 0

t.onkey(go_up, 'Up')
t.onkey(go_down, 'Down')
t.onkey(go_right, 'Right')
t.onkey(go_left, 'Left')









while True:

    coords = []
    for i in snake:
        coords.append(i.pos())


    snake_head.setpos(snake_head.pos()[0] + cell * snakex, snake_head.pos()[1] + cell * snakey)


    for index, part in enumerate(snake[1:]):

        if index == 0:
            part.goto(coords[0])
        else:
            part.goto(coords[index])

    sleep(0.1)

    t.listen()


t.mainloop()

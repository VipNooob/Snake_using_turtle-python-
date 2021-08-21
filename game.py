import sys
import turtle as t
from random import choice
from time import sleep


# field settings
cell = 50
# quantity of cells in width
width = 16
# quantity of cells in length
length = 12

window = t.Screen()
window.setup(cell * width + 120, cell * length + 120)


# window._root.resizable(False, False)
window.bgcolor('black')
window.title('CODDY snake')
window.tracer(0)


# build a grid on a field
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



def get_grid_coordinates():
    field = []

    for l in range(length):

        if l != 0:
            y = y - cell
        else:
            y = cell * (length / 2) - cell / 2

        for w in range(width):

            if w != 0:
                x = x + cell
            else:
                x = -cell * (width / 2) + cell / 2

            coordinates = (x, y)
            field.append(coordinates)

    return field




def spawn_apple(snake):
    field = get_grid_coordinates()

    for i in snake:
        x_snake = i.pos()[0]
        y_snake = i.pos()[1]
        snake_coords = (x_snake, y_snake)
        if snake_coords in field:
            field.remove(snake_coords)


    apple_coordinates = choice(field)
    apple.setpos(apple_coordinates[0], apple_coordinates[1])
    apple.showturtle()




# create an initial snake
snake_head = t.Turtle()
snake_body1 = t.Turtle()
snake_body2 = t.Turtle()
snake_body3 = t.Turtle()

snake_head.color('grey')
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

# movement direction
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
    window.tracer(0)
    # create a list of coordinates of the snake blocks (previous position)
    coords = []
    for i in snake:
        coords.append(i.pos())

    # check collision between a snake head and borders
    if ((snake_head.pos()[0] + cell * snakex) - (cell / 2)) < -(width / 2) * cell:
        sys.exit()

    if ((snake_head.pos()[0] + cell * snakex) + (cell / 2)) > (width / 2) * cell:
        sys.exit()


    if ((snake_head.pos()[1] + cell * snakey) + (cell / 2)) > (length / 2) * cell:
        sys.exit()


    if ((snake_head.pos()[1] + cell * snakey) - (cell / 2)) < -(length / 2) * cell:
        sys.exit()


    # move a snake head in the new posiotion
    snake_head.setpos(snake_head.pos()[0] + cell * snakex, snake_head.pos()[1] + cell * snakey)


    for i in snake[1:]:
        if snake[0].pos() == i.pos():
            sys.exit()

    # move other parts of the snake
    for index, part in enumerate(snake[1:]):
        part.goto(coords[index])
    # show a new added block of the snake
    snake[-1].showturtle()


    # check collision between a snake head and an apple
    if (snake[0].pos()[0] == apple.pos()[0]) and (snake[0].pos()[1] == apple.pos()[1]):


        apple.hideturtle()
        snake_part = add_block()
        snake.append(snake_part)

        spawn_apple(snake)



    t.listen()
    sleep(0.2)





    window.update()
























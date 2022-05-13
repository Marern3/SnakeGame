"""Snake, classic arcade game.

Author: Humberto Alejandro Rosas Téllez
Author2: Mariana Edith Ramírez Navarrete
"""

from random import randrange
from re import X
from tkinter import Y
from turtle import *

from freegames import square, vector

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)


def change(x, y):
    """Change snake direction."""
    aim.x = x
    aim.y = y


def inside(head):
    """Return True if head inside boundaries."""
    return -200 < head.x < 190 and -200 < head.y < 190
#Crea función global inside de food para establecer los límites de Food en el tablero
def inside(food):
    """Return True if food inside boundaries."""
    return -200 < food.x < 190 and -200 < food.y < 190    


def move():
    """Move snake forward one segment."""
    head = snake[-1].copy() 
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food: #El snake se come la comida
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10 #Reposicionar la comida en un nuevo lugar aleatorio
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9, 'black')

    "           Mover comida        "
    food.x += randrange(-1, 2,1) * 10 
    food.y += randrange(-1, 2,1) * 10

    #CHECK SI LA COMIDA SALE DEL MUNDO

     #si no está dentro de los límites, el cuadro verde, Food, se genera en una nueva posición random
    if not inside(food):
        food.x = randrange(-1, 2,1) * 10 
        food.y = randrange(-1, 2,1) * 10      
        square(food.x, food.y, 9, 'green') #X=0, Y=0, tanmaño 9        

    square(food.x, food.y, 9, 'green') #X=0, Y=0, tanmaño 9
    update() #borra pantalla
    ontimer(move, 100) #velocidad


setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()

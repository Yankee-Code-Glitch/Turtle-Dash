from turtle import *
import random
import time

def moveup():
    player.left(90)
    player.forward(15)
    player.right(90)
def movedown():
    player.right(90)
    player.forward(15)
    player.left(90)

def startwindow():
    global Window
    Window = Screen()
    Window = title("Pyng")
    Window = bgcolor("#0b005e")
    Window = setup(1000,450)
    onkeypress(moveup,"Up")
    onkeypress(movedown,"Down")
    listen()
    
def barProperties():
    global topBar
    topBar = Turtle()
    topBar.hideturtle()
    topBar.shape("square")
    topBar.pensize(15)
    topBar.color("#0073d8")
    
    global lowerBar
    lowerBar = Turtle()
    lowerBar.hideturtle()
    lowerBar.shape("square")
    lowerBar.pensize(15)
    lowerBar.color("#0073d8")
    
def playerProperties():
    global player
    player = Turtle()
    player.shapesize(3)
    player.color("#d6d6d6")


startwindow()
barProperties()
playerProperties()

player.penup()
player.hideturtle()
player.goto(-450,0)
player.showturtle()
player.speed(9999)

topBar.up()
topBar.hideturtle()
topBar.goto(460,190)
topBar.down()
topBar.goto(-465,190)

lowerBar.up()
lowerBar.hideturtle()
lowerBar.goto(-465,-190)
lowerBar.down()
lowerBar.goto(465,-190)



asteroids = []

while True:
    Position = int(random.randint(-180,180))
    i = 0
    asteroid = Turtle()
    asteroid.hideturtle()
    asteroid.penup()
    asteroid.goto(450,Position)
    asteroid.left(180)
    asteroid.speed(2)
    asteroid.shape("circle")
    asteroid.shapesize(3)
    asteroid.color("#7c7c7c")
    asteroid.showturtle()



    asteroids.append(asteroid)

    for rock in asteroids:
        rock.forward(80)


Example = asteroids.asteroid("ejemplo",Position)
Example.forward(10)
print(Position)

mainloop()
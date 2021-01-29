from turtle import *
import random
import time

def moveup():
    if player.ycor() + 15 <= 185:
        player.left(90)
        player.forward(15)
        player.right(90)
        
def movedown():
    if player.ycor() - 15 >= -185:
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
i = 5
Bolean = True
while Bolean:
    Position = int(random.randint(-180,180))

    if i%5 == 0:
        asteroid = Turtle()
        asteroid.hideturtle()
        asteroid.penup()
        asteroid.goto(450,Position)
        asteroid.left(180)
        asteroid.speed(20)
        asteroid.shape("circle")
        asteroid.shapesize(3)
        asteroid.color("#7c7c7c")
        asteroid.showturtle()
    i = random.randint(0,10)


    asteroids.append(asteroid)

    for rock in asteroids:
        if rock.distance(player)<20:
            gameOvermessage = Turtle()
            gameOvermessage.speed(0)
            gameOvermessage.shape("square")
            gameOvermessage.color("white")
            gameOvermessage.penup()
            gameOvermessage.hideturtle()
            gameOvermessage.goto(0,0)
            gameOvermessage.write("Game Over", align="center", font=("courier","50","normal"))
            player.hideturtle()
            Bolean = False
            for rock in asteroids:
                rock.hideturtle()
        rock.forward(random.randint(10,200))

mainloop()

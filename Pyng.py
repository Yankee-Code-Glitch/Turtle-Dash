from turtle import *
def moveup():
    player.left(90)
    player.forward(15)
    player.right(90)
def movedown():
    player.right(90)
    player.forward(15)
    player.left(90)

def startwindow():
    Window = Screen()
    Window = title("Pyng")
    Window = bgcolor("#0b005e")
    Window = setup(1000,450)
    onkeypress(moveup,"Up")
    onkeypress(movedown,"Down")
    listen()
    
def barProperties():
    topBar = Turtle()
    topBar.shape("square")
    topBar.pensize(15)
    topBar.color("#0073d8")
    
    lowerBar = Turtle()
    lowerBar.shape("square")
    lowerBar.pensize(15)
    lowerBar.color("#0073d8")
    
def playerProperties():
    player = Turtle()
    player.shapesize(3)
    player.color("#d6d6d6")
    

    
startwindow()
barProperties()
playerProperties()

topBar = Turtle()
topBar.up()
topBar.hideturtle()
topBar.goto(460,190)
topBar.down()
topBar.goto(-465,190)

lowerBar = Turtle()
lowerBar.up()
lowerBar.hideturtle()
lowerBar.goto(-465,-190)
lowerBar.down()
lowerBar.goto(465,-190)

player = Turtle()
player.penup()
player.hideturtle()
player.goto(-450,0)
player.showturtle()
player.speed(9999)


mainloop()

from turtle import *
def moveup():
    player.left(90)
    player.forward(15)
    player.right(90)
def movedown():
    player.right(90)
    player.forward(15)
    player.left(90)


Window = Screen()
Window = title("Pyng")
Window = bgcolor("#0b005e")
Window = setup(1000,450)

topBar = Turtle()
topBar.shape("square")
topBar.pensize(15)
topBar.color("#0073d8")
topBar.up()
topBar.hideturtle()
topBar.goto(460,190)
topBar.down()
topBar.goto(-465,190)

lowerBar = Turtle()
lowerBar.shape("square")
lowerBar.pensize(15)
lowerBar.color("#0073d8")
lowerBar.up()
lowerBar.hideturtle()
lowerBar.goto(-465,-190)
lowerBar.down()
lowerBar.goto(465,-190)

player = Turtle()
player.shapesize(3)
player.color("#d6d6d6")
player.penup()
player.hideturtle()
player.goto(-450,0)
player.showturtle()
player.speed(9999)

onkeypress(moveup,"Up")
onkeypress(movedown,"Down")
listen()
mainloop()

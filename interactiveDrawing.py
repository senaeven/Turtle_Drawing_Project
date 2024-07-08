import turtle

drawingBoard = turtle.Screen() #() koymak çalıştır demek.
drawingBoard.bgcolor("light blue")
drawingBoard.title("Drawing Board")

turtleInstance = turtle.Turtle()

def turtleForward():
    turtleInstance.forward(100)

def turtleRight():
    turtleInstance.right(10)

def turtleLeft():
    turtleInstance.left(10)

def clearScreen():
    turtleInstance.clear()

def returnHome():
    turtleInstance.penup()
    turtleInstance.home()
    turtleInstance.pendown()

def penUp():
    turtleInstance.penup()

def penDown():
    turtleInstance.pendown()


drawingBoard.listen()
drawingBoard.onkey(fun=turtleForward, key="space")
drawingBoard.onkey(fun=turtleRight, key="Up")
drawingBoard.onkey(fun=turtleLeft, key="Down ")
drawingBoard.onkey(fun=clearScreen, key="BackSpace")
drawingBoard.onkey(fun=returnHome, key="h")

turtle.mainloop()
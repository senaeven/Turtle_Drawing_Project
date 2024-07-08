import turtle

turtleScreen = turtle.Screen()
turtleScreen.bgcolor("red")
turtleScreen.title("Shrinking Squares")

turtleInstance = turtle.Turtle()
turtleInstance.color("white")

def shrinkingSquares(size):
    for i in range(4):
        turtleInstance.forward(size)
        turtleInstance.left(90)
        size = size - 5

shrinkingSquares(200)
shrinkingSquares(170)
shrinkingSquares(140)
shrinkingSquares(110)
shrinkingSquares(80)
shrinkingSquares(50)
shrinkingSquares(20)
turtle.done()



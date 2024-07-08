import turtle

board = turtle.Screen()
board.bgcolor("blue")
board.title("Star")
turtleInstance = turtle.Turtle()
sides = int(input("kenar sayısını girin: "))
angle = 360.0 / sides
sideLength = 50

for i in range(sides):
    turtleInstance.right(angle)
    turtleInstance.forward(sideLength)


turtle.done()
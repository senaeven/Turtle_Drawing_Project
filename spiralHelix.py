import turtle

turtleScreen = turtle.Screen()
turtleScreen.bgcolor("yellow")
turtleInstance = turtle.Turtle()
turtleScreen.title("ölmek istiyorum")
turtleColors = ["red","purple","blue","green","orange"]
turtle.speed(10) #hızı ayarlama

for i in range(10):
    turtleInstance.color(turtleColors[i % 5]) #out of range hatası almamak için
    turtleInstance.circle(10*i)
    turtleInstance.circle(-10*i)
    turtleInstance.left(i)

turtle.mainloop() #turtle.done yerine kullanılabilir
#turtle.done() #screen kapanmasın diye
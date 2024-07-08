import turtle
import random

screen = turtle.Screen()
screen.bgcolor("light blue")
FONT = ("Arial",25,"normal")
GRID_SIZE= 10
score = 0
game_over = False

#turtles list
turtle_list = []

#score turtle
scoreTurtle = turtle.Turtle()

#countdown turtle
countdown_turtle = turtle.Turtle()
def setup_score_turtles():
    scoreTurtle.hideturtle() #turtle ı gizleme
    scoreTurtle.color("red")
    scoreTurtle.penup()

    topHeight = screen.window_height() / 2
    y = topHeight * 0.9
    scoreTurtle.setpos(0,y)
    scoreTurtle.write(arg="Score:0", move=False, align="center", font=FONT)

def make_turtle(x,y):
    t = turtle.Turtle()

    def handle_click(x,y):
        global score
        score += 1
        scoreTurtle.clear()
        scoreTurtle.write(arg=f"Score:{score}", move=False, align="center", font=FONT)

    t.onclick(handle_click)
    t.penup()
    t.shape("turtle")
    t.shapesize(2,2)
    t.color("dark green")
    t.goto(x * GRID_SIZE,y * GRID_SIZE)
    turtle_list.append(t)

x_coordinates = [-20, -10, 0, 10, 20]
y_coordinates = [-20, -10, 0, 10, 20]

def setup_turtles():
    for x in x_coordinates:
        for y in y_coordinates:
            make_turtle(x,y)

def hide_turtles():
    for t in turtle_list:
        t.hideturtle()

#recursive functs varsa bi if kontrolü olmalı exit için.
def show_turtles_randomly():
    if not game_over:
        hide_turtles()
        random.choice(turtle_list).showturtle()
        screen.ontimer(show_turtles_randomly, 500)

def countdown(time):
    global game_over
    countdown_turtle.hideturtle()
    countdown_turtle.color("black")
    scoreTurtle.penup()
    topHeight = screen.window_height() / 2
    y = topHeight * 0.9
    countdown_turtle.setpos(0, y - 30)
    countdown_turtle.clear()

    if time > 0:
        countdown_turtle.clear()
        countdown_turtle.write(arg=f"Time:{time}", move=False, align="center", font=FONT)
        screen.ontimer(lambda: countdown(time-1),1000)
    else:
        game_over = True
        countdown_turtle.clear()
        hide_turtles()
        countdown_turtle.write(arg="Game over! ", move=False, align="center", font=FONT)

turtle.tracer(0)

setup_turtles()
setup_score_turtles()
hide_turtles()
show_turtles_randomly()
countdown(10)
turtle.tracer(1)  #tracer ı kullanmak animasyonları sıfırladı. çat diye açılıyo.

turtle.mainloop()


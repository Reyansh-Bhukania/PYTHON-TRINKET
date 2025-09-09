import turtle
import random
import time

# Screen setup

screen = turtle.Screen()
screen.bgcolor("skyblue")
screen.setup(width=800, height=600)
screen.tracer(0)

# Player setup

dart = turtle.Turtle()
dart.shape("triangle")
dart.color("red")
dart.penup()
dart.goto(0, -250)
dart.setheading(90)

# Score display

score = 0

score_display = turtle.Turtle()
score_display.hideturtle()
score_display.penup()
score_display.goto(-380, 260)
score_display.color("black")
score_display.write("Score: {}".format(score), font=("Arial", 16, "normal"))

# Balloon list

balloons = []

# Game variables

game_speed = 0.02
difficulty_increase = 0.001
spawn_interval = 2
last_spawn_time = time.time()
running = True

 

# Functions

def move_left():

    x = dart.xcor() - 30

    if x > -390:

        dart.setx(x)

 

def move_right():

    x = dart.xcor() + 30

    if x < 390:

        dart.setx(x)

def spawn_balloons():
    balloon=turtle.Turtle()
    balloon.shape("square")
    balloon.color(random.choice(["blue","green","yellow","red","pink","grey"]))
    balloon.penup()
    balloon.goto(random.randint(-350,350),random.randint(100,300))
    balloon.speed=random.uniform(1,3)

    if random.random()<0.2:
        balloon.color("black")
        balloon.is_bomb=True
    else:
        balloon.is_bomb=False
    
    balloons.append(balloon)




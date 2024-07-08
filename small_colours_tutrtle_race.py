# More Turtle Graphics, Event Listeners, State and Multiple Instances

from turtle import *

# tim = Turtle(shape="turtle")
screen = Screen()

# def move_forward():
#     tim.forward(10)
# def move_backward():
#     tim.backward(10)
# def turn_right():
#     new_heading=tim.heading()-10
#     tim.setheading(new_heading)
# def turn_left():
#     tim.setheading(tim.heading()+10)
# def clear():
#     tim.clear()
#     tim.penup()
#     tim.home()
#     tim.pendown()

# screen.listen()
# screen.onkey(move_forward,"w")
# screen.onkey(move_backward,"s")
# screen.onkey(turn_right,"a")
# screen.onkey(turn_left,"d")
# screen.onkey(clear,"c")

# timmy=Turtle()
# tommy=Turtle()
# timmy.color("purple")
# tommy.color("blue")

# Turtle Race

colours = ['red','orange','yellow','green','blue','indigo','purple']

import random

is_race=False
all_turtles =[]
screen.setup(width=500,height=400)
user_colour=screen.textinput(title="Make Your Bet", prompt="Which turtle will win the race? Enter a color: ")
# print(user_colour)
for tur_i in range(0,7):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colours[tur_i])
    new_turtle.goto(x=-230,y=-100+20*tur_i)
    all_turtles.append(new_turtle)

if user_colour:
    is_race=True
while is_race:
    for turtle in all_turtles:
        if turtle.xcor()>230:
            is_race=False
            winning_colour=turtle.pencolor()
            if winning_colour==user_colour:
                print(f"You've won! The {winning_colour} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_colour} turtle is the winner!")
        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)

 

screen.exitonclick()





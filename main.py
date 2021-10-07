import turtle
from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make a bet", prompt="Which turtle will win the race? Enter a color: ")

is_game_on = False

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_postion = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for i in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[i])
    new_turtle.goto(x=-230, y=y_postion[i])
    all_turtles.append(new_turtle)

if user_bet:
    is_game_on = True

while is_game_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_game_on = False
            win_turtle_color = turtle.pencolor()
            if win_turtle_color == user_bet:
                print(f"You've win!! The winner is *****{win_turtle_color} turtle*****")
            else:
                print(f"You've lost!! The winner is *****{win_turtle_color} turtle*****")

        random_dis = random.randint(0, 10)
        turtle.forward(random_dis)


screen.exitonclick()

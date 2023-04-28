from turtle import Turtle, Screen

import random

is_race_on = False
screen = Screen()
screen.setup(width = 500, height = 400)
user_bet = screen.textinput(title = "Make your bet", prompt = "Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

turtles = []

y_coordinate = -100


for turtle_index in range(0, 6):
    new_turtle = Turtle(shape = "turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x = -225, y = y_coordinate)
    turtles.append(new_turtle)
    y_coordinate += 40
 
if user_bet:
    is_race_on = True


while is_race_on:
    for turtle in turtles:
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)
        if turtle.xcor() >= 220:
            winner = turtle.pencolor()
            is_race_on = False
            if winner == user_bet:
                print(f"You won! The {winner} turtle is the winner!")
            else:
                print(f"You lost! The {winner} turtle is the winner!")





screen.exitonclick()
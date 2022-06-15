# It's time to race

from turtle import Turtle, Screen
import random

# create a flag for while loop
is_race = False

# enable screen and set the turtle specs
screen = Screen()
screen.setup(width=500, height=400)
colours = ["Red", "Green", "Purple", "Blue", "Yellow", "Orange"]

# take the user bet
user_turtle = screen.textinput(title="Make your bet", prompt=f"Enter the colour of a turtle among {colours} which is going to win :")
# print(user_turtle)
turtle_list = []

# Set the turtle positions
y_position = [-75, -45, -15, 15, 45, 75]

# create the required number of turtles for the set positions
for turtle_index in range(0, 6):
    turtle_name = Turtle(shape="turtle")
    turtle_name.penup()
    turtle_name.color(colours[turtle_index])
    turtle_name.goto(x=-230, y=y_position[turtle_index])
    turtle_list.append(turtle_name)

# print(turtle_list)

# check for the
if user_turtle:
    is_race = True


while is_race:

    for turtle in turtle_list:

        if int(turtle.xcor()) >= 230:
            is_race = False
            winning_turtle = turtle.pencolor()
            print(turtle_name.pencolor())
            if user_turtle == winning_turtle:
                print(f"You won! The {winning_turtle} won the race!")
            else:
                print(f"You lost! The {winning_turtle} won the race!")

        turtle.forward(random.randint(0, 10))

screen.exitonclick()
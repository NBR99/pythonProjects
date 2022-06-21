# Welcome to python Snake Game!

from turtle import Screen, Turtle
from snake import Snake
import time
# Step-1 : Setting up the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("Black")
screen.title("Snake Game!")
screen.tracer(0)

snake = Snake()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()



































screen.exitonclick()
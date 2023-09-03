from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake_game = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(snake_game.up, "w")
screen.onkey(snake_game.right, "d")
screen.onkey(snake_game.left, "a")
screen.onkey(snake_game.down, "s")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake_game.move()
    # testing collision with the food object
    if snake_game.head.distance(food) < 15:
        snake_game.extend()
        score.increase_score()
        food.refresh()



    # TODO ditect collision with a wall
    if (snake_game.head.xcor() > 290 or snake_game.head.xcor() < -290 or snake_game.head.ycor() > 290 or snake_game.head
            .ycor() < -290):
        game_on = False
        score.game_over()

    # TODO detecting collision with snake tail.

    for segment in snake_game.body[1:]:
        if snake_game.head.distance(segment) < 10:
            game_on = False
            score.game_over()

screen.exitonclick()

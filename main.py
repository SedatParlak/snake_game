from turtle import Screen
from snake import Snake
from food import Food
import time
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")
screen.onkey(snake.down, "Down")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extent()
        scoreboard.score_increase()
        scoreboard.update_score()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()
        scoreboard.update_score()
        scoreboard.data_write()
        game_is_on = False
        scoreboard.game_over()

    for turtle in snake.turtles:
        if turtle == snake.turtles[0]:
            pass
        elif snake.head.distance(turtle) < 10:
            scoreboard.reset()
            scoreboard.update_score()
            scoreboard.data_write()
            game_is_on = False
            scoreboard.game_over()





















screen.exitonclick()
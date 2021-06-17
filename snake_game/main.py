import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Score


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Score()


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    # 食べ物との衝突
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # 壁との衝突
    if snake.head.xcor() > 280 or snake.head.xcor() < - \
            280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        # game_is_on = False
        scoreboard.reset()
        snake.reset()

    # 頭がボディにぶつかったら終わり
    # for segment in snake.segments:
    #     if segment == snake.head:
    #         pass
    #     elif snake.head.distance(segment) < 10:
    #         # game_is_on = False
    #         scoreboard.reset()
    #         snake.reset()

    # スライス使用上と同じ
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.reset()
            snake.reset()


screen.exitonclick()

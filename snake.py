import turtle
from turtle import Screen
from snakeclass import Snake
import time as t
from foodclass import Food
from score import Score

s = Screen()
s.bgcolor("black")
s.setup(width=600, height=600)
s.tracer(0)
s.listen()
score = Score()
sna = Snake()
f = Food()


def up():
    if sna.lis[0].heading() != 270:
        sna.lis[0].setheading(90)


def down():
    if sna.lis[0].heading() != 90:
        sna.lis[0].setheading(270)


def left():
    if sna.lis[0].heading() != 0:
        sna.lis[0].setheading(180)


def right():
    if sna.lis[0].heading() != 180:
        sna.lis[0].setheading(0)


turtle.onkey(key="Up", fun=up)
turtle.onkey(key="Down", fun=down)
turtle.onkey(key="Right", fun=right)
turtle.onkey(key="Left", fun=left)
game_over = 0
while not game_over:
    s.update()
    t.sleep(0.1)
    sna.move()
    if sna.lis[0].distance(f) < 15:
        f.move()
        sna.add_segment()
        score.increase()
        s.update()

    elif sna.lis[0].xcor() > 280 or sna.lis[0].xcor() < -295 or sna.lis[0].ycor() > 280 or sna.lis[0].ycor() < -280:
        score.game_over()
        game_over = 1
    for i in sna.lis[1::]:
        if sna.lis[0].distance(i) < 10:
            score.game_over()
            game_over = 1

s.exitonclick()

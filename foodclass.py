import random as r
from turtle import Turtle


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.move()
        self.color("yellow")
        self.shape("circle")
        self.shapesize(stretch_wid=0.6, stretch_len=0.6)
        self.speed("fastest")

    def move(self):
        x = r.randint(-280, 280)
        y = r.randint(-280, 280)
        self.goto(x, y)

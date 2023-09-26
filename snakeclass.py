from turtle import Turtle

COR = [(0, 0), (-20, 0), (-40, 0)]


class Snake:
    def __init__(self):
        self.lis = []
        self.create_snake()

    def create_snake(self):
        for i in COR:
            t = Turtle()
            t.penup()
            t.setpos(i)
            t.color("yellow")
            t.shape("circle")
            self.lis.append(t)

    def move(self):
        for rr in range(len(self.lis) - 1, 0, -1):
            x = self.lis[rr - 1].xcor()
            y = self.lis[rr - 1].ycor()
            self.lis[rr].goto(x, y)
        self.lis[0].forward(20)

    def add_segment(self):
        x = self.lis[-1].xcor()
        y = self.lis[-1].ycor()
        t = Turtle()
        t.penup()
        t.color("yellow")
        t.shape("circle")
        self.lis.append(t)
        self.lis[-1].goto(x, y)

from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def up(self, limit = 350):
        self.goto(self.xcor(), min(limit, int(self.ycor() + 20)))

    def down(self, limit = -350):
        self.goto(self.xcor(), max(limit, int(self.ycor() - 20)))
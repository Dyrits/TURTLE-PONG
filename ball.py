from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.speed = 100

    def collide(self, x = None, y = None):
        if x is not None and y is not None and abs(self.xcor() - x) < 20 and abs(self.ycor() - y) < 50:
            self.bounce_x()
            self.bounce_y()
        elif y is None and x is not None and abs(self.xcor()) > abs(x):
            self.reset_position()
            self.bounce_x()
            return True
        elif x is None and y is not None and abs(self.ycor()) > abs(y):
            self.bounce_y()

    def move(self):
        x = self.xcor() + self.x_move
        y = self.ycor() + self.y_move
        self.goto(x, y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.speed = int(self.speed * 1.1)

    def reset_position(self):
        self.goto(0, 0)
        self.speed = 100
from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.left = 0
        self.right = 0
        self.color("blue")
        self.penup()
        self.hideturtle()
        self.goto(0, 370)
        self.update()

    def update(self):
        self.clear()
        self.write(f"Score: {self.left} | {self.right}", align="center", font=("Courier", 24, "normal"))

    def increase(self, side):
        if side == "left":
            self.left += 1
        elif side == "right":
            self.right += 1
        self.update()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Courier", 24, "normal"))
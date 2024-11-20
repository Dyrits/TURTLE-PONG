from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard


def game_loop():
    ball.move()
    attacker = "left" if ball.xcor() > 0 else "right"
    ball.collide(y = screen.window_height() / 2 - 20)
    scored = ball.collide(x = screen.window_width() / 2 - 20)
    if scored:
        scoreboard.increase(attacker)
        if scoreboard.left == 5 or scoreboard.right == 5:
            scoreboard.game_over()
            return
        ball.reset_position()
    ball.collide(left.xcor(), left.ycor())
    ball.collide(right.xcor(), right.ycor())
    screen.update()
    screen.ontimer(game_loop, ball.speed)

if __name__ == "__main__":
    screen = Screen()
    screen.setup(width=1000, height=800)
    screen.title("Pong")
    screen.tracer(0)

    # Create the paddles
    left = Paddle((-450, 0))
    right = Paddle((450, 0))

    # Create the ball
    ball = Ball()

    # Create the scoreboard
    scoreboard = Scoreboard()
    scoreboard.update()

    # Listen for key presses
    screen.listen()
    screen.onkey(left.up, "z")  # Using AZERTY keyboard
    screen.onkey(left.down, "s")
    screen.onkey(right.up, "Up")
    screen.onkey(right.down, "Down")
    game_loop()
    screen.mainloop()
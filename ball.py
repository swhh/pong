from turtle import Turtle

SPEED = 5
DIREC = 55


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color('white')
        self.shape('circle')
        self.pu()
        self.seth(DIREC)
        self.speed('fast')
        self.direction = DIREC
        self.ball_speed = SPEED

    def move(self):
        self.forward(self.ball_speed)

    def bounce(self, wall):
        if wall:
            self.direction *= -1
            self.seth(self.direction)

        else:
            self.direction = 180 - self.direction
            self.seth(self.direction)
            self.ball_speed += 1

    def reset_position(self):
        self.goto(0, 0)
        self.bounce(False)
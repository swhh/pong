from turtle import Turtle
UP = 90
STEP = 10


class Paddle(Turtle):

    pad_num = 0

    def __init__(self, position):
        super().__init__()
        self.color('white')
        self.shape('square')
        self.pu()
        self.turtlesize(stretch_wid=1, stretch_len=4)
        self.seth(UP)
        self.goto(position)

    def up(self):
        self.forward(STEP)

    def down(self):
        self.backward(STEP)



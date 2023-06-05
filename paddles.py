from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x_position, y_position):
        super().__init__()
        self.pu()
        self.setheading(90)
        self.color("white")
        self.shapesize(stretch_len=3.5)
        self.shape("square")
        self.goto(x=x_position, y=y_position)
        self.setheading(90)

    def move_up(self):
        self.fd(20)

    def move_down(self):
        self.bk(20)

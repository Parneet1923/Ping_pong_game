from turtle import Turtle


class CenterLine(Turtle):
    def __init__(self):
        super().__init__()
        self.pu()
        self.hideturtle()
        self.color("white")
        self.setheading(270)
        self.pensize(5)
        self.goto(x=0, y=280)


    def draw_line(self):
        for i in range(27):
            self.pd()
            self.fd(20)
            self.pu()
            self.fd(20)

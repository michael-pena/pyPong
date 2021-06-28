from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, pos):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(pos)

    def go_up(self):
        if self.ycor() < 240:
            self.goto(self.xcor(), self.ycor() + 40)

    def go_down(self):
        if self.ycor() > -230:
            self.goto(self.xcor(), self.ycor() - 40)


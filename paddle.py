from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.pu()
        self.goto(position)
        self.shapesize(stretch_wid=5, stretch_len=0.5)

    def up(self):
        y_cor = self.ycor() + 20
        self.goto(self.xcor(), y_cor)

    def down(self):
        y_cor = self.ycor() - 20
        self.goto(self.xcor(), y_cor)

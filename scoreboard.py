from turtle import Turtle

ALLIGNMENT = "center"
FONT = ("Courier", 50, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.pu()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-150, 200)
        self.write(f"{self.l_score}", align=ALLIGNMENT, font=FONT)
        self.goto(150, 200)
        self.write(f"{self.r_score}", align=ALLIGNMENT, font=FONT)
        self.goto(0, 200)
        self.write(":", align=ALLIGNMENT, font=FONT)

    def l_points(self):
        self.l_score += 1
        self.update_score()

    def r_points(self):
        self.r_score += 1
        self.update_score()

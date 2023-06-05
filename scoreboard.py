from turtle import Turtle
FONT = ("Arial", 45, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.pu()
        self.player1_score = 0
        self.player2_score = 0
        self.color("white")
        self.goto(-50, 240)
        self.write(f"{self.player1_score}", align="center", font=FONT)
        self.goto(50, 240)
        self.write(f"{self.player2_score}", align="center", font=FONT)

    def player1_inc_score(self):
        self.player1_score += 1
        self.clear()
        self.write(f"{self.player1_score} : {self.player2_score}", align="center", font=FONT)

    def player2_inc_score(self):
        self.player2_score += 1
        self.clear()
        self.write(f"{self.player1_score} : {self.player2_score}", align="center", font=FONT)

    def check_winner(self):
        if self.player1_score == 6:
            self.goto(0, 0)
            self.write("Player of Left paddle wins. Game Over", align="center", font=("Arial", 25, "normal"))
            return True
        elif self.player2_score == 6:
            self.goto(0, 0)
            self.write("Player of Right paddle wins. Game Over", align="center", font=("Arial", 25, "normal"))
            return True

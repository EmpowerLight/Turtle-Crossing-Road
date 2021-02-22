from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score_x = -200
        self.score_y = 230
        self.level = 1
        self.penup()
        self.color("black")
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.goto(self.score_x, self.score_y)
        self.write(f"Level: {self.level}", align="center", font=FONT)

    def increase_level(self):
        self.level += 1
        self.clear()
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over!", align="center", font=FONT)

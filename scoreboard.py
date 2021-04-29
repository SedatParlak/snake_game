from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 14, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = self.data_read()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.write(f"Score : {self.score} High Score : {self.high_score}", align=ALIGNMENT, font=FONT)
        self.hideturtle()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0

    def data_write(self):
        with open("data.txt", "w") as file:
            file.write(str(self.high_score))

    def data_read(self):
        with open("data.txt", "r") as file:
            self.high_score = int(file.read())
        return self.high_score

    def update_score(self):
        self.clear()
        self.write(f"Score : {self.score} High Score : {self.high_score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=("Arial", 24, "normal"))

    def score_increase(self):
        self.score += 1




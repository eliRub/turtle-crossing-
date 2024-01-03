from turtle import Turtle
FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.starting_score()

    def starting_score(self):
        self.penup()
        self.hideturtle()
        self.goto(-220, 250)
        self.update_level()

    def update_level(self):
        self.clear()
        self.write(f"LEVEL: {self.level}", False, "center", FONT)

    def increase_level(self):
        self.level += 1

    def game_over(self):
        self.home()
        self.color("red")
        self.write("Game Over.", False, "center", FONT)

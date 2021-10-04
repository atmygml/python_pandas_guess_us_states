from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 10, "normal")


class Stateboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        # self.goto(0, 270)
        # self.color("white")
        self.color("black")
        # self.score = 0
        self.state_str = ""
        #self.write_score()
        self.xcoord = 0
        self.ycoord = 0

    def write_state(self, xy_coord, state_name):
        self.xcoord, self.ycoord = xy_coord
        self.goto(self.xcoord, self.ycoord)
        self.state_str = f"{state_name}"
        self.write(self.state_str, move=False, align=ALIGNMENT, font=FONT)

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", move=False, align=ALIGNMENT, font=FONT)

    # def update_score(self):
    #     self.score += 1
    #     self.clear()
    #     self.write_score()

from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.first_player_score = 0
        self.second_player_score = 0
        self.text = "{}  {}"
        self.color('white')
        self.pu()
        self.hideturtle()
        self.goto(0, 230)
        self.write_score()

    def write_score(self):
        self.write(self.text.format(self.first_player_score, self.second_player_score), True, align='center', font=('arial', 45, 'normal'))

    def update_score(self, player):
        if player:
            self.second_player_score += 1
        else:
            self.first_player_score += 1
        self.clear()
        self.setx(0)
        self.write_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER!", True, align='center', font=('arial', 34, 'normal'))
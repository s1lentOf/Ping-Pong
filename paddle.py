from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, coordinates):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.penup()
        self.goto(x=coordinates[0], y=coordinates[1])

    def go_up(self):
        new_y = self.ycor() + 30
        if new_y < 270:
            self.goto(x=self.xcor(), y=new_y)

    def go_down(self):
        new_y = self.ycor() - 30
        if new_y > -240:
            self.goto(x=self.xcor(), y=new_y)
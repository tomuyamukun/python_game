from turtle import Turtle

SIZE = [20, 100]
# POSITION = [350, 0]


class Paddle(Turtle):

    def __init__(self, x_position, y_position):
        super().__init__()
        self.shape("square")
        self.speed(0)
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.color("white")
        self.goto(x_position, y_position)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

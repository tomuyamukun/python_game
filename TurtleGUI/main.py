import turtle as t
import random

tim = t.Turtle()
tim.shape("turtle")
t.colormode(255)

# 色をランダム


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


# colours = [
#     "CornflowerBlue",
#     "DarkOrchid",
#     "IndianRed",
#     "DeepSkyBlue",
#     "LightSeaGreen",
#     "wheat",
#     "SlateGray",
#     "SeaGreen"]

# 方向とペンサイズとスピード
params = [0, 90, 180, 270]
# tim.pensize(10)
tim.speed(0)


# for _ in range(4):
#     for i in range(5):
#         tim.forward(20)
#         tim.penup()
#         tim.forward(20)
#         tim.pendown()
#     tim.right(90)


# 図形を描きながら歩く
# def draw_shape(num_side):
#     angle = 360 / num_side
#     for _ in range(num_side):
#         tim.forward(100)
#         tim.right(angle)


# for shape_side_n in range(3, 11):
#     tim.color(random.choice(colours))
#     draw_shape(shape_side_n)

# random work
# def random_work():
#     for _ in range(200):
#         tim.color(random_color())
#         tim.forward(70)
#         tim.seth(random.choice(params))


# random_work()


# 円をずらしながら
def circle_work(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        # tim.right(5)
        tim.setheading(tim.heading() + size_of_gap)
        tim.circle(100)


circle_work(5)

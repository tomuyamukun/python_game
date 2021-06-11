# import colorgram

# rgb_colors = []
# colors = colorgram.extract("image.jpg", 10)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)

# print(rgb_colors)

# ここから絵を描く作業
import random
import turtle as t

t.colormode(255)
color_list = [(233, 239, 246), (247, 239, 243), (129, 165, 205), (223, 151, 109),
              (31, 40, 60), (202, 133, 146), (139, 185, 163), (236, 214, 92)]

art = t.Turtle()
art.speed(0)
art.hideturtle()
art.penup()
art.setheading(225)
art.forward(300)
art.setheading(0)
dot_count = 0
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    dot_color = random.choice(color_list)
    art.dot(20, dot_color)
    art.forward(50)

    if dot_count % 10 == 0:
        art.setheading(90)
        art.forward(50)
        art.setheading(180)
        art.forward(500)
        art.setheading(0)


screen = t.Screen()
screen.exitonclick()

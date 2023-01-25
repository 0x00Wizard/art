import random
from turtle import Turtle, Screen

turtle = Turtle()
turtle.speed("fastest")
turtle.shape("circle")
turtle.penup()
turtle.hideturtle()
screen = Screen()
screen.colormode(255)
turtle.setheading(225)
turtle.forward(300)
turtle.setheading(0)
number_of_dots = 100


color_list = [(199, 175, 117), (125, 36, 24), (170, 106, 56), (187, 158, 51),
              (6, 57, 83), (200, 215, 204), (222, 223, 225),
              (108, 67, 85), (88, 142, 56), (20, 122, 176),
              (110, 160, 175), (76, 39, 48), (63, 153, 138),
              (9, 68, 47), (134, 41, 43), (183, 97, 79),
              (179, 201, 186), (209, 199, 129), (147, 173, 162),
              (174, 166, 169), (28, 78, 60), (210, 185, 176),
              (96, 141, 153), (19, 78, 97), (195, 189, 191),
              (139, 121, 125), (177, 197, 201)
              ]

for i in range(1, number_of_dots + 1):
    turtle.color(random.choice(color_list))
    turtle.dot(size=20)
    turtle.forward(50)
    if i % 10 == 0:
        turtle.setheading(90)
        turtle.forward(50)
        turtle.setheading(180)
        turtle.forward(500)
        turtle.setheading(0)


screen.exitonclick()

import turtle as t
import random
# import colorgram


# colours = colorgram.extract('image.jpg', 30)

# rgb = []

# for colour in colours:
#     r = colour.rgb.r
#     g = colour.rgb.g
#     b = colour.rgb.b
#     rgb.append((r,g,b))

# print(rgb)
colour_palette = [(238, 250, 244), (187, 18, 44), (243, 231, 66), (252, 235, 239), 
(210, 236, 242), (196, 75, 32), (218, 66, 107), (17, 124, 173), (196, 175, 17), 
(108, 181, 209), (12, 142, 88), (12, 166, 214), (210, 152, 96), (187, 41, 61), 
(241, 231, 2), (23, 39, 76), (77, 174, 94), (36, 44, 112), (215, 69, 50), (218, 130, 155),
(124, 185, 119), (235, 165, 183), (5, 58, 39), (146, 209, 220), (8, 95, 55), (4, 86, 111), 
(162, 29, 27), (234, 171, 164), (162, 212, 176)]

t.colormode(255)
tim = t.Turtle()
tim.penup()
tim.speed(0)
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
tim.hideturtle()

for i in range(10):
    for j in range(10):
        tim.dot(20, random.choice(colour_palette))
        tim.forward(50)
    tim.setheading(90)
    tim.forward(50)
    tim.setheading(180)
    tim.forward(500)
    tim.setheading(0)


screen = t.Screen()
screen.exitonclick()
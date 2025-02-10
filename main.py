# import colorgram
#
# colors = colorgram.extract('image.jpg',50)
# color_list = []
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     random_color = (r,g,b)
#     color_list.append(random_color)
# print(color_list)
























color_list = [(181, 171, 162), (210, 208, 205), (225, 228, 232), (228, 222, 225), (223, 229, 225),
              (184, 178, 181), (157, 80, 51), (213, 194, 153), (154, 179, 158), (37, 109, 135),
              (46, 127, 90), (180, 150, 42), (148, 175, 185), (142, 30, 22), (142, 70, 80), (217, 180, 173),
              (207, 181, 185), (207, 89, 64), (155, 22, 30), (10, 100, 77), (71, 47, 38), (95, 148, 101), (68, 150, 171), (196, 73, 81),
              (23, 64, 89), (60, 47, 54), (8, 88, 105), (181, 198, 187), (185, 192, 200), (74, 67, 45), (31, 70, 46), (30, 68, 99),
              (167, 203, 210), (111, 130, 145)]




from turtle import Turtle,Screen
import turtle
import time
import random
t = Turtle()
a = -1000
b = -1000
t.penup()
t.goto(a,b)
t.pendown()
t.circle(50,360,100)
turtle.colormode(255)
s = Screen()
x = -200
y = -200
t.penup()
t.goto(x,y)
t.pendown()
for _ in range(10):
    for _ in range(10):
        t.dot(20,random.choice(color_list))
        t.penup()
        t.forward(50)
        t.pendown()
    y += 50
    t.penup()
    t.goto(x,y)
    t.pendown()


s.exitonclick()














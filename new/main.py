from turtle import *
from colorsys import *

tracer(200)
bgcolor('black')
hideturtle()
pensize(2)

for i in range(750):
    color(hsv_to_rgb(i / 750, 1, 1)) 
    for j in range(5):
        forward(i * 0.5)
        left(160.2456)
        right(30)
        circle(i * 0.20, 70)

done()
from turtle import *
import colorsys 
import math 
import time

setup(1000, 1000)
title("Rainbow Mandala")
bgcolor("black")
colormode(1.0)
speed(0)
tracer(0)
pensize(2)
h = 0

for i in range(720):
    pencolor(colorsys.hsv_to_rgb(h, 1,1))
    right(91)

    r = 180 * math.sin(math.radians(i*4))
    circle(r)

    forward(4)
    left(89)

    update()

    time.sleep(0.03)

    h += 0.002
    if h > 1:
        h = 0

done()
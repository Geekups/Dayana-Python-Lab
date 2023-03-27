from turtle import * #pip install turtle
from colorsys import *


h= 0.8
bgcolor("black")
speed(0)
for i in range(264):
    col = hsv_to_rgb(h,1, 1)
    h+= 0.005
    color(col, col)
    begin_fill()
    circle(270 - i, 90)
    lt(90)
    circle(270 - i, 90)
    lt(10)
    end_fill()
end()
from turtle import *
bgcolor("black")
speed("fast")
pensize(14)
color("white")

def leave():
    for i in range(3):
        for i in range(3):
            fd(30)
            back(30)
            rt(45)
        lt(90)

        back(30)
        lt(45)
    rt(90)
    fd(90)

for i in range (8):
    leave()
    lt(45)
hideturtle()
done
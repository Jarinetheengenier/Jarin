#################################################################################
# Author: Arav De
# Username: Dea
#
# Assignment: A03
# Purpose: To make a more sophisticated drawing using python
# Google Doc Link: https://docs.google.com/document/d/1K3uJpF53TpgpRnpIF2t5mcx3Ka7m6H5gGJAyIjw3mGc/edit?usp=sharing
#
#################################################################################
# Acknowledgements:
#
#
#################################################################################
import random
import turtle

wn = turtle.Screen()
wn.colormode(255)
wn.bgcolor(0, 0, 70)
t = turtle.Turtle()
v = turtle.Turtle()
v.penup()
v.left(90)
v.forward(120)
v.right(90)
v.pendown()
def move_cursor(m,n):
    v.penup()
    v.left(m)
    v.forward(n)
    v.pendown()
def move_cursor1(d,g):
    t.penup()
    t.left(d)
    t.forward(g)
    t.pendown()
def main_drawing():
    v.speed(10)
    v.color('white')
    for j in range(1,3):
        if j % 2 != 0:
            v.left(45)
        else:
            v.right(30)
            move_cursor(300,300)
        for i in range(7):
            v.penup()
            f = random.randrange(100)
            v.right(f)
            v.left(f)
            v.forward(20)
            v.pendown()
            for i in range(30):
                v.right(10)
                v.forward(20)
                if i == 6:
                    move_cursor(80,80)


def human():
    t.color("white")
    move_cursor1(280,300)
    move_cursor1(90,90)
    # head
    t.seth(90)  # seth is short for set_heading, and it changes the direction t is facing.
    t.fd(30)
    t.rt(90)
    t.circle(50)
    r = t.xcor()
    y = t.ycor()
    t.pu()  # pu is short for penup. Either work, you can use them interchangeably
    t.setpos(r, y)
    t.pd()  # pd is short for pendown
    # arm 1
    t.seth(160)
    t.fd(100 / 2)
    t.rt(20)
    t.fd(100 / 2)
    t.pu()  # pu is short for penup. Either work, you can use them interchangeably
    t.setpos(r, y)
    t.pd()  # pd is short for pendown
    t.pu()  # pu is short for penup. Either work, you can use them interchangeably
    t.setpos(r, y)
    t.pd()  # pd is short for pendown

    # arm 2
    t.seth(20)
    t.fd(100 / 2)
    t.lt(20)
    t.fd(100 / 2)

    t.pu()  # pu is short for penup. Either work, you can use them interchangeably
    t.setpos(r, y)
    t.pd()  # pd is short for pendown

    # leg 1
    t.seth(270)
    t.fd(50)
    t.seth(230)
    t.fd(140 / 2)
    t.lt(40)
    t.fd(140 / 2)

    t.pu()  # pu is short for penup. Either work, you can use them interchangeably
    t.setpos(r, y)
    t.pd()  # pd is short for pendown

    # leg 2
    t.seth(270)
    t.fd(50)
    t.seth(310)
    t.fd(140 / 2)
    t.rt(40)
    t.fd(140 / 2)


def main():
    main_drawing()  # Function call to function_1
    human()
    wn.exitonclick()

main()

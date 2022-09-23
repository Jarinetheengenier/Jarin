######################################################################
# Author: Dongsoo Lee
# Username: leed
#
# Assignment: a03: Functional Turtles
#
# Purpose: To draw something complex only using functions and having a main() function called at the end of the program.
# I will be drawing Mount Everest.
######################################################################

import turtle

def background():
    skyline = turtle.Turtle()
    skyline.pencolor("skyblue")
    skyline.fillcolor("skyblue")
    skyline.speed(0)
    skyline.penup()
    skyline.goto(-350, -100)
    skyline.pendown()
    skyline.begin_fill()
    for bg in range(2):
        skyline.forward(1000)
        skyline.left(90)
        skyline.forward(400)
        skyline.left(90)
    skyline.end_fill()

def sun():
    suncircle = turtle.Turtle()
    suncircle.pencolor("orange")
    suncircle.fillcolor("orange")
    suncircle.hideturtle()
    suncircle.speed(0)
    suncircle.penup()
    suncircle.goto(200, 200)
    suncircle.pendown()
    suncircle.begin_fill()
    suncircle.circle(30, 360)
    suncircle.end_fill()

def ground():
    groundturtle = turtle.Turtle()
    groundturtle.pencolor("Gold")
    groundturtle.fillcolor("Gold")
    groundturtle.speed(0)
    groundturtle.penup()
    groundturtle.goto(-350, -100)
    groundturtle.pendown()
    groundturtle.begin_fill()
    for grounds in range(2):
        groundturtle.fd(800)
        groundturtle.right(90)
        groundturtle.fd(250)
        groundturtle.right(90)
    groundturtle.end_fill()

def pyramid1():
    #creating first pyramid
    mountainrange = turtle.Turtle()
    mountainrange.color("Black")
    mountainrange.fillcolor("Yellow")
    mountainrange.hideturtle()
    mountainrange.speed(0)
    mountainrange.penup()
    mountainrange.goto(-225, -145)
    mountainrange.pendown()
    mountainrange.begin_fill()
    for everest in range(3):
        mountainrange.fd(160)
        mountainrange.left(120)
    mountainrange.end_fill()

def pyramid2():
    #second pyramid, located behind the first one
    mountainrange = turtle.Turtle()
    mountainrange.color("Black")
    mountainrange.fillcolor("Yellow")
    mountainrange.hideturtle()
    mountainrange.speed(0)
    mountainrange.penup()
    mountainrange.goto(-140, -105)
    mountainrange.pendown()
    mountainrange.begin_fill()
    for everest in range(3):
        mountainrange.fd(160)
        mountainrange.left(120)
    mountainrange.end_fill()

def pyramid3():
    #second pyramid, located behind the first one
    mountainrange = turtle.Turtle()
    mountainrange.color("Black")
    mountainrange.fillcolor("Yellow")
    mountainrange.hideturtle()
    mountainrange.speed(0)
    mountainrange.penup()
    mountainrange.goto(-40, -130)
    mountainrange.pendown()
    mountainrange.begin_fill()
    for everest in range(3):
        mountainrange.fd(160)
        mountainrange.left(120)
    mountainrange.end_fill()

def main():

    wn = turtle.Screen()
    background()
    sun()
    ground()
    pyramid2()
    pyramid1()
    pyramid3()

    wn.exitonclick()

main()
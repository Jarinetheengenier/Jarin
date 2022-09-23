# Author:Eren Gul
# Github Username: eygul

import turtle #imports turtle library

def drawstar(bp): #draws the star

 for i in range (5):
    bp.right(144)
    bp.forward(400)
    i = i+1

def drawcircle(bp): #draws the circle
    bp.circle(210)

def main (): #imports the background image, sets up important information such as pen size, and brings the turtle to starting positions for drawing star and circle
 screen = turtle.Screen()
 screen.bgpic('image.gif')
 bp = turtle.Turtle()
 bp.pensize(7)
 bp.pencolor('red')
 bp.penup()
 bp.right(90)
 bp.forward(110)
 bp.right(90)
 bp.forward(55)
 bp.pendown()
 bp.left(72)
 drawstar(bp)
 bp.penup()
 bp.goto(-260, 170)
 bp.pendown()
 drawcircle(bp)
 screen.exitonclick()

main()



############################################################################
# Author: Ali Ramazani
# Username: ramazanim
# Google Doc Web Address: https://docs.google.com/document/d/1yAyLk-VIuNF1LY6S-eXlb1rcqN-b7RJ8XAn8WSs8UyE/edit?usp=sharing
# Date: September 19, 2022
############################################################################

#####################################################################################
# Name: Ali Ramazani
# Username: ramazanim
# Google Doc Link: wn = https://docs.google.com/document/d/1yAyLk-VIuNF1LY6S-eXlb1rcqN-b7RJ8XAn8WSs8UyE/edit#
# Date: 09/19/2022

#####################################################################################
import turtle
import random
import time

# This function draws a circular window for night mode
def drawCircularWindowNight(t, xc, yc, shape):
    t.pencolor("#FFFFFF")
    t.pensize(2.5)
    t.setheading(0)
    t.penup()
    t.goto(xc, yc)
    t.pendown()
    t.fillcolor("#FFFF00")
    t.begin_fill()
    t.circle(shape)
    t.left(90)
    t.forward(55)
    t.backward(50)
    t.speed(1.5)
    t.forward(23)
    t.backward(5.5)
    t.right(90)
    t.forward(23)
    t.backward(46)
    t.end_fill()

# This function creates a square window for night mode
def drawSquareWindowNight(t, xc, yc):
    t.pencolor("#FFFFFF")
    t.pensize(2.5)
    t.setheading(0)
    t.penup()
    t.goto(xc, yc)
    t.pendown()
    t.fillcolor("#000000")
    t.begin_fill()
    side = 1
    for i in range(4):
        side = side + 1
        t.forward(40)
        t.right(90)
    t.forward(20)
    t.right(90)
    t.forward(40)
    t.backward(20)
    t.right(90)
    t.forward(20)
    t.backward(40)

    t.end_fill()

#This function creates a moon for night mode
def drawMoon(t, xc, yc, shape):
    t.pensize(3.5)
    t.setheading(0)
    t.fillcolor("#FFFFFF")
    t.penup()
    t.goto(xc,yc)
    t.begin_fill()
    t.pendown()
    t.circle(shape)
    t.end_fill()

#This function creates the poster for day mode
def drawPoster(t, xc, yc):
    t.penup()
    t.goto(xc, yc)
    t.pencolor("#000000")
    t.pendown()
    t.setheading(0)
    t.left(90)
    t.forward(120)

    posterFrame = t.position()
    t.right(90)
    t.forward(20)
    t.right(90)
    t.forward(120)
    t.right(90)
    t.forward(20)

    t.goto(posterFrame)
    t.setheading(90)
    t.right(90)
    t.forward(90)
    t.right(90)
    t.forward(70)
    t.right(90)
    t.forward(64)

    t.write("************\n************\nOn Sale\n$1000,000", font=("Arial", 10, "bold"))


# This function creates the trees
def drawTree(t, xc, yc):
    t.setheading(90)
    t.speed(15)
    t.fillcolor("#013f28")
    t.penup()
    t.goto(xc, yc)
    t.pendown()
    t.begin_fill()

    t.pencolor("#013f28")
    for i in range(10):
        t.circle(20)
        t.right(36)
        t.forward(10)
    t.end_fill()
    t.setheading(90)

# This function creates the chimney
def drawChimney(t, xc, yc):
    t.pencolor("#000000")
    t.pensize(2.5)
    t.penup()
    t.goto(xc, yc)
    t.pendown()
    t.left(90)
    t.forward(20)
    t.right(90)
    t.forward(20)
    t.right(90)
    t.forward(70)
    t.right(90)
    t.forward(20)
    t.right(90)
    t.forward(70)


# This function creates a square window for day mode
def drawSquareWindow(t, xc, yc):
    t.pencolor("#FFFFFF")
    t.pensize(2.5)
    t.setheading(0)
    t.penup()
    t.goto(xc, yc)
    t.pendown()
    t.fillcolor("#87ceeb")
    t.begin_fill()
    side = 1
    for i in range(4):
        side = side + 1
        t.forward(40)
        t.right(90)
    t.forward(20)
    t.right(90)
    t.forward(40)
    t.backward(20)
    t.right(90)
    t.forward(20)
    t.backward(40)

    t.end_fill()

# This function creates a circular window for day mode
def drawCircularWindow(t, xc, yc, shape):
    t.pencolor("#FFFFFF")
    t.pensize(2.5)
    t.setheading(0)
    t.penup()
    t.goto(xc, yc)
    t.pendown()
    t.fillcolor("#87CEEB")
    t.begin_fill()
    t.circle(shape)
    t.left(90)
    t.forward(55)
    t.backward(50)
    t.speed(1.5)
    t.forward(23)
    t.backward(5.5)
    t.right(90)
    t.forward(23)
    t.backward(46)
    t.end_fill()

# This funtion draws a sun in day mode
def drawSun(t, xc, yc, shape):
    t.pensize(3.5)
    t.setheading(0)
    t.fillcolor("#FFFF00")
    t.penup()
    t.goto(xc,yc)
    t.begin_fill()
    t.pendown()
    t.circle(shape)
    t.end_fill()

# This function draws a door for the house
def drawDoor(t, xc, yc):
    t.pensize(2.5)
    t.penup()
    t.goto(xc,yc)
    t.fillcolor("#800000")
    t.begin_fill()
    t.setheading(90)

    for i in range(2):
        t.forward(100)
        t.right(90)
        t.forward(70)
        t.right(90)

    t.end_fill()

# This function draws a door knob
def drawKnob(t, xc, yc, sz):
    t.color("#EEE8AA")
    t.penup()
    t.goto(xc, yc)
    t.pendown()
    t.circle(sz)
    t.fillcolor("#FFFFFF")
    t.begin_fill()
    t.end_fill()

# This function draws the house
def drawHouse(t):
    t.color(0, 0, 0)
    t.pensize(2.5)
    t.penup()
    t.goto(-220,-10)
    t.pendown()
    t.setheading(90)
    t.fillcolor("#27285C")
    t.begin_fill()
    t.forward(200)
    roofone = t.position()
    t.right(90)
    t.forward(400)
    rooftwo = t.position()
    t.right(90)
    t.forward(200)
    t.right(90)
    t.forward(400)
    t.right(90)
    t.end_fill()

    #roof
    t.penup()
    t.goto(roofone)
    t.fillcolor("#FAF9F6")
    t.begin_fill()
    t.pendown()
    t.goto(-25,350)
    t.goto(rooftwo)
    t.end_fill()
    t.setheading(90)

# This function executes the program
def main():
    wn = turtle.Screen()
    wn.bgcolor("#87CEEB")
    wn.title("House on Sale: Buy Soon or You'll Lose it! (Maximize the Screen) ")
    t = turtle.Turtle()
    t.speed(10)

    name = input("What's your name? ")
    print(name, ",Welcome to Legends Real Estate! We're glad you've chosen us to buy your dream home")
    select = input("We have one house for sale now. It's in California. To see the house in day mode, press 1 and for night mode press 2. ")
    if select == "1":
        time.sleep(3)
        drawSun(t, -220, 180, 60)
        drawChimney(t, 145, 220)
        drawHouse(t)
        drawDoor(t, -65, -10)
        drawKnob(t, -5, 40, 5)
        drawCircularWindow(t, -20, 137, 25)
        drawSquareWindow(t, -200, 185)
        drawSquareWindow(t, 100, 185)
        drawTree(t, -200, -1)
        drawPoster(t, 230,-1)
        drawTree(t, -210, -150)
        drawTree(t, 180, -150)
    elif select == "2":
        time.sleep(3)
        wn.bgcolor("black")
        drawMoon(t, -220, 180, 60)
        drawChimney(t, 145, 220)
        drawHouse(t)
        drawDoor(t, -65, -10)
        drawKnob(t, -5, 40, 5)
        drawCircularWindowNight(t, -20, 137, 25)
        drawSquareWindowNight(t, -200, 185)
        drawSquareWindowNight(t, 100, 185)
        drawTree(t, -200, -1)
        drawPoster(t, 230, -1)
        drawTree(t, -210, -150)
        drawTree(t, 180, -150)
     #   drawStars(t, 180, -150)



    wn.exitonclick()


main()

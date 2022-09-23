
#################################################################################
# Author: Savannah McCoy
# Username: mccoys2
#
# Assignment: A03:  Fully Functional Gitty Psychedelic Robotic Turtles
# Purpose: To use our knowledge on the turtle library and to practice creating more complex designs using turtles.
# Google Doc Link: https://docs.google.com/document/d/13_QiXqwmfMt4YrXqVjelQCJw50HgBYfhiUzg1iPgqlg/edit?usp=sharing
#################################################################################
# Acknowledgements: My cat, Peach, who found out how to uninstall the pycharm app.
#
#
##################################################################################

import turtle

def bonkfunc(bonk):

    """"
    Displays text in the screen
    """
    bonk.penup()
    bonk.hideturtle()
    bonk.left(135)
    bonk.forward(400)
    bonk.left(135)
    bonk.forward(200)
    bonk.write("C0MPUT3R SCI3NC3", font=[50])

def smileyfunc(smiley):

    """
    Creates a smiley face
    """

    smiley.penup()      #moves the turtle to the position
    smiley.left(45)
    smiley.forward(150)
    smiley.left(45)

    smiley.pendown()
    smiley.forward(50) #creates the left eye of the smiley face

    smiley.penup()      #moves the turtle to the position
    smiley.right(90)
    smiley.forward(80)
    smiley.right(90)

    smiley.pendown()
    smiley.forward(50)  #creates the right eye of the smiley face

    smiley.penup()  #moves the turtle to the position
    smiley.forward(50)
    smiley.left(90)
    smiley.forward(50)
    smiley.left(90)
    smiley.forward(20)
    smiley.right(180)

    smiley.pendown()    #creates the smile of the smiley face
    smiley.forward(20)
    smiley.right(90)
    smiley.forward(175)
    smiley.right(90)
    smiley.forward(20)


def wavefunc(wave):

    """"
    Creates computer screens and fills them with color
    """

    wave.begin_fill()
    for i in range(4):  #creates the bottom rectangle and fills it
        wave.forward(300)
        wave.right(90)
        wave.forward(200)
        wave.right(90)

    wave.color('#101F3B')
    wave.end_fill()
    wave.left(90)
    wave.begin_fill()

    for i in range(4): #creates the top rectangle and fills it
        wave.begin_fill()
        wave.forward(200)
        wave.right(90)
        wave.forward(300)
        wave.right(90)
        wave.end_fill()

    wave.color('#1E3C73')
    wave.end_fill()

def keysfunc(keys):
    """
    Creates keys of the keyboard
    """
    keys.color('#535E73')

    for i in range(7): #creates the vertical lines of the keys
        keys.forward(20)
        keys.right(90)
        keys.forward(200)
        keys.left(90)
        keys.forward(20)
        keys.left(90)
        keys.forward(200)
        keys.right(90)

    keys.forward(22)
    keys.right(90)
    keys.forward(80)

    for i in range(5): #creates horizontal lines of the keys
        keys.right(90)
        keys.forward(300)
        keys.left(90)
        keys.forward(20)
        keys.left(90)
        keys.forward(300)
        keys.right(90)

def main():
    """"
    Contains all the main things
    """

    wn = turtle.Screen()
    wn.bgcolor('lightblue')
    wave = turtle.Turtle()
    bonk = turtle.Turtle()
    keys = turtle.Turtle()
    smiley = turtle.Turtle()
    smiley.color('yellow')
    smiley.pensize(10)
    keys.pensize(10)
    keys.speed(10)
    wave.speed(10)
    wave.pensize(15)

    wavefunc(wave)  #calling all functions
    keysfunc(keys)
    smileyfunc(smiley)
    bonkfunc(bonk)
    wn.exitonclick()

main()
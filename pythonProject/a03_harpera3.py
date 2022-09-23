#################################################################################
# Author: Alyssa Harper
# Username: harpera3
#
# Assignment: A03: A Pair of Fully Functional Gitty Psychedelic Robotic Turtles
# Purpose:
# Google Doc Link: https://docs.google.com/document/d/17ISwAUH2yFw6j9XQdgZDV7q5kOBLKS8_pyiw0z4P1KQ/edit?usp=sharing
#
#################################################################################
# Acknowledgements:
#
#
#################################################################################

import turtle


def function_1():
    # This function is for petals of a daisy
    x = 0
    aj = turtle.Turtle()
    aj.pensize(2)
    aj.color('pink')
    aj.speed(0)
    while x < 15:
        aj.left(8)
        aj.forward(70)
        aj.right(55)
        aj.forward(15)
        aj.right(90)
        aj.forward(15)
        aj.right(55)
        aj.forward(70)
        x = x + 1
    pass

def function_3():
    # For the stem of the flower

    ally = turtle.Turtle()
    ally.pencolor('green')
    ally.pensize(3)
    ally.right(90)
    ally.fd(250)

    # For the dirt
    jim = turtle.Turtle()
    jim.penup()
    jim.right(90)
    jim.fd(250)
    jim.left(90)
    jim.fd(250)
    jim.pendown()
    jim.color('brown')
    jim.backward(500)

    pass



def function_2():
    max = turtle.Turtle()
    max.penup()
    max.backward(300)
    max.left(90)
    max.forward(200)
    max.write('Oopsy Daisy', True, font=("Arial", 50, 'normal'))
    # This function is for the words

    pass



def main():
    wn = turtle.Screen()       # Creating the screen and making it a different color
    wn.colormode(1)
    wn.bgcolor(.3, .1, .5)


    function_1()            # Function call to function_1
    function_2()            # Function call to function_2
    function_3()            # Function call to function_3
    wn.exitonclick()

main()



######################################################################
# Author: Oussema Khlifi
# Username: khlifio
#
# Assignment: A03: Functional turtles
#purpose: building a house
#Google Doc:https://docs.google.com/document/d/1i_m3DeFWuXpmA2y0ko1dtr6ZNCcPZPuS4lVrh8mdue0
#################################################################################
import turtle
def rectangle(a):
    ''' a function that builds a triangle'''
    for i in ['blue','white', 'green', 'red']:
        a.color(i)
        a.fd(200)
        a.left(90)

def eqtriangle(a):
    ''' a function that builds an equilateral triangle'''
    for i in ['yellow','purple', 'cyan']:
        a.color(i)
        a.fd(100)
        a.left(120)

def buildhouse(a):
    ''' a function that builds the house: a rectangle + a set of triangles'''
    a.width(10)
    rectangle(a)
    #now, we will set up the right position to start building the triangles
    a.penup()
    a.fd(100)
    a.left(90)
    a.fd(200)
    a.left(-90)
    a.pendown()
    # finally, this will be our starting point for our set of triangles
    eqtriangle(a)
    a.penup()
    a.right(-120)
    a.pendown()
    eqtriangle(a)
    a.penup()
    a.fd(100)
    a.right(120)
    a.pendown()
    eqtriangle(a)
    turtle.penup()

def this_is_my_house():
    ''' a function that displays the text: welcome to my house! '''
    turtle.setpos(90,-100) # setting up the coordinates
    turtle.color('black')
    turtle.write('Welcome to my house !', font=('Arial', 40, 'italic'), align='center') #displaying the text message


def main():
    oussema = turtle.Turtle()
    wn = turtle.Screen()
    wn.colormode(255)  # setting up the colormode to RBG mode
    wn.bgcolor(100, 140, 120)
    buildhouse(oussema)
    this_is_my_house()
    turtle.hideturtle()
    turtle.exitonclick()

main()



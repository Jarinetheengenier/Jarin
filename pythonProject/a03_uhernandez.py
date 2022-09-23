#########################################################################
# Name: Ulises Hernandez
# Username: HernandezU
# https://docs.google.com/document/d/1cLFjBuJFDiD0bzBMZlL51teBzQg1ZLqrpn1sH8vTWbw/edit?pli=1#
#########################################################################

import turtle

turtle.colormode(255)


def make_sun(peter):

    """
    Draws the sun in the top left corner.

    param peter: a Turtle object
    :return: None
"""

    peter.penup()
    peter.setpos(-280, 380)
    peter.pendown()
    peter.color("yellow")
    peter.begin_fill()
    peter.right(60)
    peter.circle(-130, 180)
    peter.end_fill()
    peter.penup()
    peter.setpos(-268, 283)
    peter.pendown()


def drawthreeRays(peter):
    """

    param peter: this simply draws the rays to the sun
    :return: none
    """
    peter.pensize(2)
    peter.right(120)
    peter.forward(100)
    peter.penup()                   # I had to set each ray in three different positions
    peter.setpos(-290, 240)
    peter.pendown()
    peter.right(45)
    peter.forward(100)
    peter.penup()
    peter.setpos(-326, 208)
    peter.pendown()
    peter.right(42)
    peter.forward(100)
    peter.penup()


def cloud(clouds):
    """

    param clouds: this simply draws a cloud
    :return:
    """
    clouds.color('white')
    clouds.penup()
    clouds.setpos(180, 170)
    clouds.pendown()
    clouds.begin_fill()
    clouds.right(90)
    for i in range(4):
        clouds.circle(50, 180)
        clouds.left(-90)
    clouds.end_fill()


def buildings(building):
    """

    :param building: this draws two twin skyscrapers
    :return: none
    """
    building.color('grey')
    building.penup()
    building.setpos(120, -20)
    building.pendown()
    building.begin_fill()
    building.forward(255)
    building.left(180)
    building.forward(260)
    building.left(90)
    building.forward(300)
    building.left(90)
    building.forward(20)
    building.left(90)
    building.forward(280)
    building.right(90)
    building.forward(250)
    building.left(90)
    building.forward(20)
    building.end_fill()
    building.penup()
    building.setpos(134, -41)
    building.color('brown')
    building.pendown()
    building.begin_fill()
    building.right(90)
    building.forward(250)
    building.right(90)
    building.forward(300)
    building.right(90)
    building.forward(247.5)
    building.right(90)
    building.forward(280)
    building.end_fill()
    building.penup()
    building.setpos(-125, -20)
    building.color('grey')
    building.right(-180)
    building.pendown()
    building.begin_fill()
    building.forward(255)
    building.left(180)
    building.forward(255)
    building.left(90)
    building.forward(300)
    building.left(90)
    building.forward(20)
    building.left(90)
    building.forward(280)
    building.right(90)
    building.forward(290)
    building.left(90)
    building.forward(21)
    building.end_fill()
    building.penup()                # I made the code to where it looks like a mirror reflection
    building.setpos(-145, -42)
    building.color('brown')
    building.pendown()
    building.begin_fill()
    building.right(90)
    building.forward(280)
    building.right(90)
    building.forward(330)
    building.right(90)
    building.forward(282)
    building.right(90)
    building.forward(330)
    building.end_fill()
    building.penup()


def windows(glass):
    """

    param glass: it creates the windows for the skyscrapers
    :return: none
    """
    glass.pensize(5)
    glass.pencolor(230, 102, 150)
    glass.fillcolor(170, 90, 220)               # the time I utilize the rgb function
    glass.penup()
    glass.setpos(171, -85)
    glass.pendown()
    glass.begin_fill()
    for i in range(2):
        glass.forward(45)
        glass.right(90)
        glass.forward(45)
        glass.right(90)
        glass.forward(45)
        glass.right(90)
        glass.forward(45)
        glass.right(90)
        glass.penup()
        glass.forward(115)
        glass.pendown()
    glass.end_fill()
    glass.penup()
    glass.setpos(171, -205)
    glass.pendown()
    glass.begin_fill()
    for i in range(2):
        glass.forward(45)
        glass.right(90)
        glass.forward(45)
        glass.right(90)
        glass.forward(45)
        glass.right(90)
        glass.forward(45)
        glass.right(90)
        glass.penup()
        glass.forward(115)
        glass.pendown()
    glass.end_fill()
    glass.penup()
    glass.setpos(-344, -85)
    glass.pendown()
    glass.begin_fill()
    for i in range(2):                  # this is where I made the same eight windows with four on each skyscraper
        glass.forward(45)
        glass.right(90)
        glass.forward(45)
        glass.right(90)
        glass.forward(45)
        glass.right(90)
        glass.forward(45)
        glass.right(90)
        glass.penup()
        glass.forward(115)
        glass.pendown()
    glass.end_fill()
    glass.penup()
    glass.setpos(-344, -205)
    glass.pendown()
    glass.begin_fill()
    for i in range(2):
        glass.forward(45)
        glass.right(90)
        glass.forward(45)
        glass.right(90)
        glass.forward(45)
        glass.right(90)
        glass.forward(45)
        glass.right(90)
        glass.penup()
        glass.forward(115)
        glass.pendown()
    glass.end_fill()


def spider_web(web):
    """

    param web: creates a spider web that's attached to the left skyscraper
    :return:
    """
    web.penup()
    web.setpos(-300, -166)
    web.color('white')
    web.pensize(2)
    web.pendown()
    for i in range(6):
        web.forward(75)
        web.penup()
        web.left(120)
        web.forward(20)
        web.left(90)
        web.pendown()
    web.penup()
    web.setpos(-265, -153)
    web.pendown()
    web.circle(13)
    web.penup()
    web.setpos(-265, -143)
    web.pendown()
    web.circle(25)


def spider_man(spidey):
    """

    param spidey: this makes the spider-man mask
    :return: none
    """
    spidey.pencolor('black')
    spidey.fillcolor('red')
    spidey.begin_fill()
    spidey.circle(60)
    spidey.end_fill()
    spidey.left(90)
    spidey.pencolor('grey')
    for i in range(6):
        spidey.forward(120)
        spidey.penup()
        spidey.left(120)
        spidey.forward(30)
        spidey.left(90)
        spidey.pendown()
    spidey.penup()
    spidey.setpos(-12, 56)
    spidey.pendown()
    spidey.circle(13)
    spidey.penup()
    spidey.setpos(-37, 58)
    spidey.pendown()
    spidey.circle(39)
    spidey.penup()
    spidey.setpos(-39, 74)
    spidey.pendown()
    spidey.fillcolor('white')          # the two lenses from the mask are parallel to each other
    spidey.pencolor('black')
    spidey.begin_fill()
    spidey.left(15)
    spidey.forward(30)
    spidey.left(90)
    spidey.forward(24)
    spidey.right(135)
    spidey.end_fill()
    spidey.penup()
    spidey.setpos(40, 74)
    spidey.pendown()
    spidey.fillcolor('white')
    spidey.begin_fill()
    spidey.left(15)
    spidey.forward(30)
    spidey.right(90)
    spidey.forward(24)
    spidey.right(135)
    spidey.end_fill()


def make_text(peter, txt):
    """
    Writes text to the screen.

    param peter: a Turtle object
    :return: None
    """
    peter.color("blue")
    peter.setpos(0, 260)
    peter.write(txt, move=False, align='center', font=("italic", 20, ("bold", "normal")))


def main():
    """
    this draws every function in order of list
    :return: none
    """
    wn = turtle.Screen()
    wn.bgcolor("lightblue")
    wn.title("Spider-Man")
    peter = turtle.Turtle()
    peter.hideturtle()
    clouds = turtle.Turtle()
    clouds.hideturtle()
    building = turtle.Turtle()
    building.hideturtle()
    glass = turtle.Turtle()
    glass.hideturtle()
    web = turtle.Turtle()
    web.hideturtle()
    spidey = turtle.Turtle()
    spidey.hideturtle()
    make_sun(peter)
    drawthreeRays(peter)
    cloud(clouds)
    buildings(building)
    windows(glass)
    spider_web(web)
    spider_man(spidey)
    make_text(peter, "Spider-Man 4")            # text in turtle

    wn.exitonclick()


main()
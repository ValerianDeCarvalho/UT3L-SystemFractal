import turtle

def lSystemTurtle(turtle, lSystem):
    x=175
    for i in lSystem:
        if i == 'A':
            turtle.color("blue")
            turtle.forward(x)

        elif i == 'B':
            turtle.color("purple")
            for i in range (3):
                turtle.forward(x/2)
                turtle.right(90)
            turtle.forward(x/2)
            x=x*0.95

        elif i == 'C':
            turtle.right(185)

def initialisationTurtle():
    screen = turtle.Screen()
    screen.setup(width=800, height=600)
    screen.title("L-System Turtle Graphics")
    screen.bgcolor("white")
    theturtle = turtle.Turtle()
    theturtle.speed(10)
    return theturtle

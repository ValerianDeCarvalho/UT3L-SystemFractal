from LSystem import LSystem
from Turtle import Turtle
from Tkinter import Tkinter,TkinterGet

def main():
    Tkinter.window()
    axiome = TkinterGet.axiome
    tuple = TkinterGet.rules
    iteration = TkinterGet.iteration
    lsystem = LSystem.lSystemCreate(axiome, tuple, iteration)
    myturtle = Turtle.initialisationTurtle()
    Turtle.lSystemTurtle(myturtle, lsystem)

main()
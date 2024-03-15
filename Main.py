import LSystem
import Turtle
import Tkinter

def main():
    Tkinter.window()
    axiome = Tkinter.axiome
    dictionnaire = Tkinter.dictionnaire
    iteration = Tkinter.iteration
    lsystem = LSystem.lSystemCreate(axiome, dictionnaire, iteration)
    myturtle = Turtle.initialisationTurtle()
    Turtle.lSystemTurtle(myturtle, lsystem)

main()
from LSystem import LSystem
from Turtle import Turtle
from Tkinter import Tkinter,TkinterGet

def main():
    # Créer une fenêtre Tkinter pour obtenir les paramètres de l'utilisateur
    Tkinter.window()
    
    # Récupérer les valeurs de l'axiome, des règles et du nombre d'itérations
    axiome = TkinterGet.axiome
    tuple = TkinterGet.rule
    iteration = TkinterGet.iteration

    # Créer la chaîne L-System
    lsystem = LSystem.lSystemCreate(axiome, tuple, iteration)

    # Initialiser la tortue et dessiner la chaîne L-System
    myturtle = Turtle.initialisationTurtle()
    
    # Dessiner la chaîne L-System
    Turtle.lSystemTurtle(myturtle, lsystem)

main()
import turtle
from Tkinter import TkinterGet

def lSystemTurtle(turtle, lSystem):
    stack = []  # Pile pour stocker les positions
    x = 10  # Longueur du déplacement

    # Dictionnaire des couleurs associées aux symboles
    colors = {
        'A': "blue",
        'B': "red",
        'C': "purple",
        'D': "yellow",
        'E': "green"
    }

    # Dictionnaire des valeurs associées aux symboles
    vals = {
        'A': TkinterGet.valA,
        'B': TkinterGet.valB,
        'C': TkinterGet.valC,
        'D': TkinterGet.valD, 
        'E': TkinterGet.valE  
    }
    
    # Parcourir chaque symbole de la chaîne L-System et effectuer l'action correspondante
    for i in lSystem:
        turtle.color(colors[i])  # Changer la couleur du stylo en fonction du symbole (avec le dictionnaire colors)
        if vals[i] == 0:
            turtle.forward(x)  # Avancer de x unités
        elif vals[i] == 1:
            turtle.left(25)  # Tourner à gauche de 25
        elif vals[i] == 2:
            turtle.right(25)  # Tourner à droite de 25
        elif vals[i] == 3:
            stack.append(turtle.position())  # Empiler la position actuelle
        elif vals[i] == 4:
            pos = stack.pop()  # Dépiler la dernière position
            turtle.goto(pos)  # Se déplacer vers la position dépliée

# Initialisation de la tortue et de la fenêtre graphique
def initialisationTurtle():
    screen = turtle.Screen()  # Créer une fenêtre graphique
    screen.setup(width=800, height=600)  # Définir la taille de la fenêtre
    screen.title("L-System Turtle Graphics")  # Définir le titre de la fenêtre
    screen.bgcolor("white")  # Définir la couleur de fond de la fenêtre
    theturtle = turtle.Turtle()  # Créer une tortue
    theturtle.speed(9)  # Définir la vitesse de la tortue
    theturtle.left(90)  # Tourner la tortue vers la gauche
    return theturtle  # Retourner la tortue
import turtle
import LsConfig

def turtleRun(turtle, lSystem, grRules,speed):
    turtle.reset() # on remet la tortue à l'état initial, on efface l'écran
    turtle.left(90)  # Tourner la tortue vers la gauche en position initiale
    turtle.speed(speed)
    stack = []  # Pile pour stocker les positions
    # Parcourir chaque symbole de la chaîne L-System et effectuer l'action correspondante
    for i in lSystem:
        rule=grRules[i]
        if rule.command==LsConfig.predefined_options[0] :
            if rule.rot!="":
                rot=int(rule.rot)
                if rot<0:
                    turtle.right(-rot)
                elif rot>0:
                    turtle.left(rot)
            if rule.len!="":
                len=int(rule.len)
                if len<0:
                    turtle.backward(-len)
                elif len>0:
                    turtle.forward(len)
        elif rule.command==LsConfig.predefined_options[1] :
            stack.append(turtle.position())  # Empiler la position actuelle
        elif rule.command==LsConfig.predefined_options[2] :
            if stack:
                pos = stack.pop()  # Dépiler la dernière position
                turtle.penup()
                turtle.goto(pos)  # Se déplacer vers la position dépliée
                turtle.pendown()
            else:
                print("Stack is empty")


# Initialisation de la tortue et de la fenêtre graphique
def turtleInit():
    screen = turtle.Screen()  # Créer une fenêtre graphique
    
    screen.setup(width=800, height=600)  # Définir la taille de la fenêtre
    screen.title("L-System Turtle Graphics")  # Définir le titre de la fenêtre
    screen.bgcolor("white")  # Définir la couleur de fond de la fenêtre
    
    theturtle = turtle.Turtle()  # Créer une tortue
    theturtle.left(90)  # Tourner la tortue vers la gauche en position initiale

    return theturtle  # Retourner l'ecran et la tortue

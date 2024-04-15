# Importation des modules nécessaires
from LSystem import LSystem  # Module pour créer la chaîne L-System
from Turtle import Turtle    # Module pour dessiner avec turtle
from Tkinter import Tkinter, TkinterGet  # Modules pour l'interface graphique Tkinter

def main():
    # Créer une fenêtre Tkinter pour obtenir les paramètres de l'utilisateur
    Tkinter.window()
    
    # Récupérer les valeurs de l'axiome, des règles et du nombre d'itérations à partir des champs d'entrée de l'interface graphique
    axiome = TkinterGet.axiome
    rule = TkinterGet.rule
    iteration = TkinterGet.iteration

    # Créer la chaîne L-System en utilisant les valeurs récupérées
    lsystem = LSystem.lSystemCreate(axiome, rule, iteration)

    # Initialiser la tortue pour dessiner
    myturtle = Turtle.initialisationTurtle()
    
    # Dessiner la chaîne L-System en utilisant turtle
    Turtle.lSystemTurtle(myturtle, lsystem) 

# Appel de la fonction principale pour démarrer le programme
main()
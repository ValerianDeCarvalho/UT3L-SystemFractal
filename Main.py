# Importation des modules nécessaires
import Ls  # Module pour créer la chaîne L-System
import LsTurtle    # Module pour dessiner avec turtle
import LsUi  # Modules pour l'interface graphique Tkinter
import tkinter as tk

def main():

    # Initialisation du contexte graphique    
    root = tk.Tk()
    root.title("lSystem")
    root.attributes('-fullscreen', True)
    root.eval('tk::PlaceWindow . center')  # Centrer la fenêtre sur l'écran

    # Initialiser la fenetre de la tortue
    myturtle = LsTurtle.turtleInit()
    
    # Créer une fenêtre Tkinter pour obtenir les paramètres de l'utilisateur
    LsUi.create_ui_window(root,myturtle)

    # Lancer les fenêtres
    root.mainloop()

# Appel de la fonction principale pour démarrer le programme
main()




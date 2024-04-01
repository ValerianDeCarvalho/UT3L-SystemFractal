import tkinter as tk
from Tkinter import TkinterGet

def window():
    # Création de la fenêtre principale
    window = tk.Tk()
    window.title("lSystem")
    window.geometry("400x300")  
    window.eval('tk::PlaceWindow . center')  # Centrer la fenêtre sur l'écran

    # Affichage du label pour l'itération
    label_iteration = tk.Label(window, text="Itérations:")
    label_iteration.pack()
    # Entrée pour l'itération
    iteration = tk.Entry(window, width=75)
    iteration.insert(0, "4")  # Mettre une valeur par défaut
    iteration.pack()

    # Affichage du label pour l'axiome
    label_axiom = tk.Label(window, text="Axiome:")
    label_axiom.pack()
    # Entrée pour l'axiome
    axiom = tk.Entry(window, width=75)
    axiom.insert(0, "A")  # Mettre une valeur par défaut
    axiom.pack()

    # Affichage du label pour les règles
    label_rules = tk.Label(window, text="Règles:")
    label_rules.pack()
    # Entrée pour les règles
    rules = tk.Entry(window, width=75)
    rules.insert(0, 'A,AACDCABABAEBDBACACAE')  # Mettre une valeur par défaut
    rules.pack()

    # Création des labels et des boutons pour chaque lettre
    labels = ['A', 'B', 'C', 'D', 'E']
    for label_text in labels:

        # Affichage du label pour la lettre
        label = tk.Label(window, text=label_text)
        label.pack()

        # Création d'un cadre(frame) pour les boutons
        frame = tk.Frame(window)
        frame.pack()

        # Création des boutons pour chaque lettre et leur associer une commande
        button_texts = ["Avancer", "Gauche", "Droite", "Sauvegarder", "Charger"]
        # Utilisation de la fonction enumerate pour itérer sur une liste et obtenir à la fois l'indice et la valeur de chaque élément
        for i, button_text in enumerate(button_texts):
            # Definir la commande en fonction de la lettre du label
            if label_text == 'A':
                command = lambda v, i=i, label_text=label_text: TkinterGet.ValueA(i)
            elif label_text == 'B':
                command = lambda v, i=i, label_text=label_text: TkinterGet.ValueB(i)
            elif label_text == 'C':
                command = lambda v, i=i, label_text=label_text: TkinterGet.ValueC(i)
            elif label_text == 'D':
                command = lambda v, i=i, label_text=label_text: TkinterGet.ValueD(i)
            elif label_text == 'E':
                command = lambda v, i=i, label_text=label_text: TkinterGet.ValueE(i)
                
            # Créer le bouton avec la commande associée et le texte du bouton
            button = tk.Button(frame, text=button_text, command=lambda c=command, v=label_text: c(v))
            button.pack(side=tk.LEFT)

    # Boutton pour envoyer les valeurs et les récupérer dans TkinterGet
    button_send = tk.Button(window, text="Envoyer", command=lambda: TkinterGet.recupererValeur(iteration, axiom, rules, window))
    button_send.pack()

    # Lancer la fenêtre
    window.mainloop()
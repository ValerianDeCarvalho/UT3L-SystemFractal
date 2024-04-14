import tkinter as tk
from Tkinter import TkinterGet

def window():
    # Création de la fenêtre principale
    window = tk.Tk()
    window.title("lSystem")
    window.geometry("400x300")  
    window.eval('tk::PlaceWindow . center')  # Centrer la fenêtre sur l'écran

    # Séparateur
    separator = tk.Label(window, text="")
    separator.pack()

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
    rules.insert(0, 'A,B')  # Mettre une valeur par défaut
    rules.pack()

    # Séparateur
    separator = tk.Label(window, text="")
    separator.pack()

    # Création des labels et des boutons pour chaque lettre
    labels = ['A', 'B', 'C', 'D', 'E']
    for label_text in labels:

        # Affichage du label pour la lettre
        if label_text == 'A':
            labela = tk.Label(window, text=label_text + ":" + renommerValeur(TkinterGet.valA))
            labela.pack()
        elif label_text == 'B':
            labelb = tk.Label(window, text=label_text + ":" + renommerValeur(TkinterGet.valB))
            labelb.pack()
        elif label_text == 'C':
            labelc = tk.Label(window, text=label_text + ":" + renommerValeur(TkinterGet.valC))
            labelc.pack()
        elif label_text == 'D':
            labeld = tk.Label(window, text=label_text + ":" + renommerValeur(TkinterGet.valD))
            labeld.pack()
        elif label_text == 'E':
            labele = tk.Label(window, text=label_text + ":" + renommerValeur(TkinterGet.valE))
            labele.pack()

        # Création d'un cadre(frame) pour les boutons
        frame = tk.Frame(window)
        frame.pack()

        # Création des boutons pour chaque lettre et leur associer une commande
        button_texts = ["Avancer", "Gauche", "Droite", "Sauvegarder", "Charger"]
        # Utilisation de la fonction enumerate pour itérer sur une liste et obtenir à la fois l'indice et la valeur de chaque élément
        for i, button_text in enumerate(button_texts):
            # Definir la commande en fonction de la lettre du label
            if label_text == 'A':
                # Utilisation de lambda pour créer une fonction anonyme avec des arguments
                command = lambda v, i=i, label_text=label_text: (TkinterGet.ValueA(i), updatelabel(labela, "A:" + renommerValeur(i)))
            elif label_text == 'B':
                command = lambda v, i=i, label_text=label_text: (TkinterGet.ValueB(i), updatelabel(labelb, "B:" + renommerValeur(i)))
            elif label_text == 'C':
                command = lambda v, i=i, label_text=label_text: (TkinterGet.ValueC(i), updatelabel(labelc, "C:" + renommerValeur(i)))
            elif label_text == 'D':
                command = lambda v, i=i, label_text=label_text: (TkinterGet.ValueD(i), updatelabel(labeld, "D:" + renommerValeur(i)))
            elif label_text == 'E':
                command = lambda v, i=i, label_text=label_text: (TkinterGet.ValueE(i), updatelabel(labele, "E:" + renommerValeur(i)))
                
            # Créer le bouton avec la commande associée et le texte du bouton
            # Ce bouton appelle la fonction associée à la lettre du label avec la valeur i (0, 1, 2, 3, 4)
            button = tk.Button(frame, text=button_text, command=lambda c=command, v=label_text: c(v))
            button.pack(side=tk.LEFT)
    
    # Séparateur
    separator = tk.Label(window, text="")
    separator.pack()

    # Bouton pour envoyer les valeurs et les récupérer dans TkinterGet
    button_predefined1 = tk.Button(window, text="Prédéfini1", command=lambda: (predefined1(axiom, rules, iteration), updatelabel(labela, "A:" + renommerValeur(TkinterGet.valA)), updatelabel(labelb,"B" + renommerValeur(TkinterGet.valB)), updatelabel(labelc, "C:" + renommerValeur(TkinterGet.valC)), updatelabel(labeld, "D" + renommerValeur(TkinterGet.valD)), updatelabel(labele, "E:" + renommerValeur(TkinterGet.valE)) ))
    button_predefined1.pack()

    # Séparateur
    separator = tk.Label(window, text="")
    separator.pack()

    # Bouton pour envoyer les valeurs et les récupérer dans TkinterGet
    button_send = tk.Button(window, text="Envoyer", command=lambda: TkinterGet.recupererValeur(iteration, axiom, rules, window))
    button_send.pack()

    # Lancer la fenêtre
    window.mainloop()

# Mettre à jour le texte d'un label
def updatelabel(label, text):
    label.config(text=text)

def predefined1(axiom, rules, iteration):
    axiom.delete(0, 'end')
    axiom.insert(0, "A")
    rules.delete(0, 'end')
    rules.insert(0, 'A,AACDCABABAEBDBACACAE')
    iteration.delete(0, 'end')
    iteration.insert(0, "4")
    TkinterGet.valA = 0
    TkinterGet.valB = 1
    TkinterGet.valC = 2
    TkinterGet.valD = 3
    TkinterGet.valE = 4

def renommerValeur(ABCDE):
    if ABCDE == 0:
        return " Avancer"
    elif ABCDE == 1:
        return " Gauche"
    elif ABCDE == 2:
        return " Droite"
    elif ABCDE == 3:
        return " Sauvegarder"
    elif ABCDE == 4:
        return " Charger"
import tkinter as tk
from Tkinter import TkinterGet,TkinterPredefined

def window():
    # Création de la fenêtre principale
    window = tk.Tk()
    window.title("lSystem")
    window.geometry("400x300")  
    window.eval('tk::PlaceWindow . center')  # Centrer la fenêtre sur l'écran

    # Séparateur
    separator = tk.Label(window, text="")
    separator.pack()

    # Affichage du gros titre
    label_title = tk.Label(window, text="L-System", font=("Arial", 24, "bold"), relief="raised", bd=5)
    label_title.pack()

    # Séparateur
    separator = tk.Label(window, text="")
    separator.pack()

    # Création d'une frame pour regrouper les labels d'itération et de l'axiome
    frame_labelia = tk.Frame(window)
    frame_labelia.pack()
    # Création d'une frame pour regrouper les entrées d'itération et de l'axiome
    frame_inputia = tk.Frame(window)
    frame_inputia.pack()

    # Affichage du label pour l'itération
    label_iteration = tk.Label(frame_labelia,padx=35, text="Itérations:")
    label_iteration.pack(side=tk.LEFT)
    # Entrée pour l'itération
    iteration = tk.Entry(frame_inputia, width=20)
    iteration.insert(0, "4")  # Mettre une valeur par défaut
    iteration.pack(side=tk.LEFT)

    # Affichage du label pour l'axiome
    label_axiom = tk.Label(frame_labelia,padx=30, text="Axiome:")
    label_axiom.pack(side=tk.LEFT)
    # Entrée pour l'axiome
    axiom = tk.Entry(frame_inputia, width=20)
    axiom.insert(0, "A")  # Mettre une valeur par défaut
    axiom.pack(side=tk.LEFT)

    # Affichage du label pour les règles
    label_rules = tk.Label(window, text="Règles:")
    label_rules.pack()
    # Entrée pour les règles
    rules = tk.Entry(window, width=40)
    rules.insert(0, 'A,B')  # Mettre une valeur par défaut
    rules.pack()

    # Création d'une frame pour regrouper les labels de rotation et de longueur
    frame_labelrl = tk.Frame(window)
    frame_labelrl.pack()
    # Création d'une frame pour regrouper les entrées de rotation et de longueur
    frame_inputrl = tk.Frame(window)
    frame_inputrl.pack()

    # Affichage du label pour la rotation
    label_rotation = tk.Label(frame_labelrl, padx=35, text="Rotation:")
    label_rotation.pack(side=tk.LEFT)
    # Entrée pour la rotation
    rotation = tk.Entry(frame_inputrl, width=20)
    rotation.insert(0, "25")
    rotation.pack(side=tk.LEFT)

    # Affichage du label pour la longueur
    label_length = tk.Label(frame_labelrl, padx=30, text="Longueur:")
    label_length.pack(side=tk.LEFT)
    # Entrée pour la longueur
    length = tk.Entry(frame_inputrl, width=20)
    length.insert(0, "10")
    length.pack(side=tk.LEFT)

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

    # Création d'une frame pour regrouper les boutons prédéfinis
    frame_predefined = tk.Frame(window)
    frame_predefined.pack(side=tk.TOP, pady=10)

    # Options pour le menu déroulant
    predefined_options = ["None","Arbre", "Arbre2", "Flocon"]

    # Variable pour stocker l'option sélectionnée
    selected_option = tk.StringVar(window)
    selected_option.set(predefined_options[0])  # Définir la première option comme sélectionnée

    # Fonction appelée lorsque l'option sélectionnée change
    def on_option_selected(event):
        option = selected_option.get()
        if option == "Arbre":
            TkinterPredefined.arbre(axiom, rules, iteration, length, rotation)
        elif option == "Arbre2":
            TkinterPredefined.arbre2(axiom, rules, iteration, length, rotation)
        elif option == "Flocon":
            TkinterPredefined.flocon(axiom, rules, iteration, length, rotation)
        updatelabel(labela, "A:" + renommerValeur(TkinterGet.valA))
        updatelabel(labelb, "B:" + renommerValeur(TkinterGet.valB))
        updatelabel(labelc, "C:" + renommerValeur(TkinterGet.valC))
        updatelabel(labeld, "D:" + renommerValeur(TkinterGet.valD))
        updatelabel(labele, "E:" + renommerValeur(TkinterGet.valE))

    # Création du menu déroulant
    dropdown_menu = tk.OptionMenu(frame_predefined, selected_option, *predefined_options, command=on_option_selected)
    dropdown_menu.pack(side=tk.LEFT, padx=5)

    # Séparateur
    separator = tk.Label(window, text="")
    separator.pack()

    # Bouton pour envoyer les valeurs et les récupérer dans TkinterGet
    button_send = tk.Button(window, text="Envoyer", command=lambda: TkinterGet.recupererValeur(iteration, axiom, rules,rotation,length,window))
    button_send.pack()

    # Lancer la fenêtre
    window.mainloop()

# Mettre à jour le texte d'un label
def updatelabel(label, text):
    label.config(text=text)

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
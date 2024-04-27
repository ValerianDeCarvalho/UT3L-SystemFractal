from tkinter import ttk
import tkinter as tk
from Tkinter import TkinterGet, TkinterPredefined, TkinterTutorial

def create_scrollbar():
    root = tk.Tk()
    root.title("lSystem")
    root.attributes('-fullscreen', True)
    root.eval('tk::PlaceWindow . center')  # Centrer la fenêtre sur l'écran

    main_frame = tk.Frame(root)
    main_frame.pack(fill=tk.BOTH, expand=1)

    # Create Frame for X Scrollbar
    sec = tk.Frame(main_frame)
    sec.pack(fill=tk.X, side=tk.BOTTOM)

    my_canvas = tk.Canvas(main_frame)
    my_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)
    x_scrollbar = ttk.Scrollbar(sec, orient=tk.HORIZONTAL, command=my_canvas.xview)
    x_scrollbar.pack(side=tk.BOTTOM, fill=tk.X)
    y_scrollbar = ttk.Scrollbar(main_frame, orient=tk.VERTICAL, command=my_canvas.yview)
    y_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    # Configure the canvas
    my_canvas.configure(xscrollcommand=x_scrollbar.set)
    my_canvas.configure(yscrollcommand=y_scrollbar.set)
    my_canvas.bind("<Configure>", lambda e: my_canvas.config(scrollregion=my_canvas.bbox(tk.ALL)))

    # Create Another Frame INSIDE the Canvas
    window = tk.Frame(my_canvas)

    my_canvas.create_window((0, 0), window=window, anchor="nw")
    return root, my_canvas, window

def window():
    # Création de la fenêtre principale
    root, my_canvas, window = create_scrollbar()

    # séparateur
    separator = tk.Label(window, text="")
    separator.pack()

    # Affichage du gros titre
    label_title = tk.Label(window, text="L-System", font=("Arial", 24, "bold"), relief="raised", bd=5)
    label_title.pack()

    # Séparateur
    separator = tk.Label(window, text="")
    separator.pack()

    # Création d'un bouton pour ouvrir une nouvelle fenêtre
    button_tutorial = tk.Button(window, text="Tutoriel", command=TkinterTutorial.open_tutorial)
    button_tutorial.pack()

    # Séparateur
    separator = tk.Label(window, text="")
    separator.pack()

    # Création d'une frame pour regrouper les labels d'itération et de l'axiome
    frame_labelia = tk.Frame(window)
    frame_labelia.pack(side=tk.TOP, anchor=tk.W)
    # Création d'une frame pour regrouper les entrées d'itération et de l'axiome
    frame_inputia = tk.Frame(window)
    frame_inputia.pack(side=tk.TOP, anchor=tk.W)

    # Affichage du label pour l'itération
    label_iteration = tk.Label(frame_labelia, padx=35, text="Itérations:")
    label_iteration.pack(side=tk.LEFT)
    # Entrée pour l'itération
    iteration = tk.Entry(frame_inputia, width=20)
    iteration.insert(0, "4")  # Mettre une valeur par défaut
    iteration.pack(side=tk.LEFT)

    # Affichage du label pour l'axiome
    label_axiom = tk.Label(frame_labelia, padx=30, text="Axiome:")
    label_axiom.pack(side=tk.LEFT)
    # Entrée pour l'axiome
    axiom = tk.Entry(frame_inputia, width=20)
    axiom.insert(0, "A")  # Mettre une valeur par défaut
    axiom.pack(side=tk.LEFT)

    # Séparateur
    separator = tk.Label(window, text="")
    separator.pack()

    # Création d'une frame pour regrouper les labels de règles
    frame_labelir = tk.Frame(window)
    frame_labelir.pack(side=tk.TOP, anchor=tk.W)
    # Création d'une frame pour regrouper les entrées de règles
    frame_inputir = tk.Frame(window)
    frame_inputir.pack(side=tk.TOP, anchor=tk.W)

    # Affichage du label pour les règles
    label_rules = tk.Label(frame_labelir, text="Règles:")
    label_rules.pack(side=tk.LEFT, anchor=tk.W)
    # Entrée pour les règles
    rules = tk.Text(frame_inputir, width=150, height=10)
    rules.insert(tk.END, "A,B")
    rules.pack(side=tk.LEFT, anchor=tk.W)

    # Séparateur
    separator = tk.Label(window, text="")
    separator.pack()

    # Création d'une frame pour le bouton DO
    frame_button_do = tk.Frame(window)
    frame_button_do.pack(side=tk.TOP, anchor=tk.W)

    # Création d'un bouton pour voir le résultat
    button_do = tk.Button(frame_button_do, text="DO", width=20, height=1)
    button_do.pack(padx=10)

    # Séparateur
    separator = tk.Label(window, text="")
    separator.pack()

    # Frame pour afficher le résultat
    frame_result = tk.Frame(window)
    frame_result.pack(side=tk.TOP, anchor=tk.W)

    # Création d'un input non éditable
    result = tk.Entry(frame_result, width=150, state='readonly')
    result.pack()

    # Séparateur
    separator = tk.Label(window, text="")
    separator.pack()

    # Frame pour afficher les trucs pour le graphique
    frame_graph = tk.Frame(window)
    frame_graph.pack(side=tk.TOP, anchor=tk.W)

    # Frame pour les boutons create et delete
    frame_buttons = tk.Frame(frame_graph)
    frame_buttons.pack(anchor=tk.W)

    def create_input():
        # Création d'un input avec un menu déroulant
        input_frame = tk.Frame(frame_graph)
        input_frame.pack(anchor=tk.W)

        input_entry = tk.Entry(input_frame, width=10)
        input_entry.pack(side=tk.LEFT)

        predefined_options = ["Dessiner", "Sauvegarder", "Charger"]
        selected_option = tk.StringVar(input_frame)
        selected_option.set(predefined_options[0])

        dropdown_menu = tk.OptionMenu(input_frame, selected_option, *predefined_options)
        dropdown_menu.config(width=20)
        dropdown_menu.pack(side=tk.LEFT)

        length_entry = tk.Entry(input_frame, width=10)
        length_entry.pack(side=tk.LEFT)
        selected_option.trace("w", lambda *args: update_input_entry(length_entry, selected_option))
        update_input_entry(length_entry, selected_option)

        rotate_entry = tk.Entry(input_frame, width=10)
        rotate_entry.pack(side=tk.LEFT)
        selected_option.trace("w", lambda *args: update_input_entry(rotate_entry, selected_option))
        update_input_entry(rotate_entry, selected_option)

    def update_input_entry(entry, option):
        if option.get() == "Dessiner":
            entry.pack(side=tk.LEFT)
        else:
            entry.pack_forget()

        # Mettre à jour la scrollbar
        my_canvas.update_idletasks()
        my_canvas.config(scrollregion=my_canvas.bbox(tk.ALL))

    # Création d'un bouton pour créer un nouvel input avec menu déroulant
    button_create_input = tk.Button(frame_buttons, text="+", command=create_input)
    button_create_input.pack(padx=10,side=tk.LEFT)

    def delete_input():
        # Supprimer le dernier input
        input_frames = frame_graph.winfo_children()
        if len(input_frames) > 1:
            input_frames[-1].destroy()

    # Création d'un bouton pour supprimer le dernier input
    button_delete_input = tk.Button(frame_buttons, text="-", command=delete_input)
    button_delete_input.pack(padx=10,side=tk.LEFT)

    # Frame
    frame_buttons = tk.Frame(window)
    frame_buttons.pack(side=tk.TOP,anchor=tk.W)

    # Bouton pour envoyer et dessiner le résultat
    button_send = tk.Button(frame_buttons, text="Envoyer")
    button_send.pack(padx=10)

    # # Création des labels et des boutons pour chaque lettre
    # labels = ['A', 'B', 'C', 'D', 'E']
    # for label_text in labels:
    #     # Affichage du label pour la lettre
    #     if label_text == 'A':
    #         labela = tk.Label(window, text=label_text + ":" + renommerValeur(TkinterGet.valA))
    #         labela.pack()
    #     elif label_text == 'B':
    #         labelb = tk.Label(window, text=label_text + ":" + renommerValeur(TkinterGet.valB))
    #         labelb.pack()
    #     elif label_text == 'C':
    #         labelc = tk.Label(window, text=label_text + ":" + renommerValeur(TkinterGet.valC))
    #         labelc.pack()
    #     elif label_text == 'D':
    #         labeld = tk.Label(window, text=label_text + ":" + renommerValeur(TkinterGet.valD))
    #         labeld.pack()
    #     elif label_text == 'E':
    #         labele = tk.Label(window, text=label_text + ":" + renommerValeur(TkinterGet.valE))
    #         labele.pack()

    #     # Création d'un cadre(frame) pour les boutons
    #     frame = tk.Frame(window)
    #     frame.pack()

    #     # Création des boutons pour chaque lettre et leur associer une commande
    #     button_texts = ["Avancer", "Gauche", "Droite", "Sauvegarder", "Charger"]
    #     # Utilisation de la fonction enumerate pour itérer sur une liste et obtenir à la fois l'indice et la valeur de chaque élément
    #     for i, button_text in enumerate(button_texts):
    #         # Definir la commande en fonction de la lettre du label
    #         if label_text == 'A':
    #             # Utilisation de lambda pour créer une fonction anonyme avec des arguments
    #             command = lambda v, i=i, label_text=label_text: (TkinterGet.ValueA(i), updatelabel(labela, "A:" + renommerValeur(i)))
    #         elif label_text == 'B':
    #             command = lambda v, i=i, label_text=label_text: (TkinterGet.ValueB(i), updatelabel(labelb, "B:" + renommerValeur(i)))
    #         elif label_text == 'C':
    #             command = lambda v, i=i, label_text=label_text: (TkinterGet.ValueC(i), updatelabel(labelc, "C:" + renommerValeur(i)))
    #         elif label_text == 'D':
    #             command = lambda v, i=i, label_text=label_text: (TkinterGet.ValueD(i), updatelabel(labeld, "D:" + renommerValeur(i)))
    #         elif label_text == 'E':
    #             command = lambda v, i=i, label_text=label_text: (TkinterGet.ValueE(i), updatelabel(labele, "E:" + renommerValeur(i)))
                
    #         # Créer le bouton avec la commande associée et le texte du bouton
    #         # Ce bouton appelle la fonction associée à la lettre du label avec la valeur i (0, 1, 2, 3, 4)
    #         button = tk.Button(frame, text=button_text, command=lambda c=command, v=label_text: c(v))
    #         button.pack(side=tk.LEFT)
    
    # Séparateur
    separator = tk.Label(window, text="")
    separator.pack()

    # Création d'une frame pour regrouper les boutons prédéfinis
    frame_predefined = tk.Frame(window)
    frame_predefined.pack(side=tk.TOP, pady=10)

    # Options pour le menu déroulant
    predefined_options = ["None","Arbre","Fleur","Flocon"]

    # Variable pour stocker l'option sélectionnée
    selected_option = tk.StringVar(window)
    selected_option.set(predefined_options[0])

    # Fonction appelée lorsque l'option sélectionnée change
    def on_option_selected(event):
        option = selected_option.get()
        if option == "None":
            TkinterPredefined.none(axiom, rules, iteration, length, rotation)
        elif option == "Arbre":
            TkinterPredefined.arbre(axiom, rules, iteration, length, rotation)
        elif option == "Flocon":
            TkinterPredefined.flocon(axiom, rules, iteration, length, rotation)
        elif option == "Fleur":
            TkinterPredefined.fleur(axiom, rules, iteration, length, rotation)
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

    # Création d'un bouton pour sauvegarder et d'un bouton pour charger
    button_save = tk.Button(window, text="Sauvegarder")
    button_save.pack(side=tk.TOP, padx=10)
    button_load = tk.Button(window, text="Charger")
    button_load.pack(side=tk.TOP, padx=10)

    # Séparateur
    separator = tk.Label(window, text="")
    separator.pack()

    # Création d'un bouton pour fermer la fenêtre
    button_close = tk.Button(window, text="Fermer", command=root.destroy)
    button_close.pack()

    # Séparateur
    separator = tk.Label(window, text="")
    separator.pack()

    # Lancer la fenêtre
    root.mainloop()

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
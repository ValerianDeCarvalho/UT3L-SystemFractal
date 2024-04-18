import tkinter as tk

# Variable pour garder une trace de l'état de la fenêtre de tutoriel
tutorial_open = False

# Fonction pour ouvrir une nouvelle fenêtre de tutoriel
def open_tutorial():
    global tutorial_open

    # Vérifier si la fenêtre de tutoriel est déjà ouverte
    if not tutorial_open:
        # Mettre à jour l'état de la fenêtre de tutoriel
        tutorial_open = True

        # Créer une nouvelle fenêtre
        tutorial_window = tk.Tk()
        tutorial_window.title("Tutorial")
        
        # Séparateur
        separator = tk.Label(tutorial_window, text="")
        separator.pack()

        # Ajouter du contenu à la fenêtre de tutoriel
        tutorial_title = tk.Label(tutorial_window, text="Tutoriel", font=("Arial", 24, "bold"), relief="raised", bd=5)
        tutorial_title.pack()

        # Séparateur
        separator = tk.Label(tutorial_window, text="")
        separator.pack()

        # Ajouter du texte d'instruction
        tutorial_text = tk.Label(tutorial_window, text="Ceci est un tutoriel pour l'application L-System!", font=("Arial", 12))
        tutorial_text.pack()

        # Séparateur
        separator = tk.Label(tutorial_window, text="")
        separator.pack()

        # Renseigner l'utilisateur sur la façon d'utiliser l'application
        tutorial_instructions = tk.Label(tutorial_window, text="Pour pouvoir utiliser l'application, veuillez remplir les champs suivants:", font=("Arial", 12))
        tutorial_instructions.pack()

        # Instructions pour les itérations
        tutorial_instructions_iteration = tk.Label(tutorial_window, text="1. Itérations: Entrez le nombre d'itérations pour générer la chaîne L-System.", font=("Arial", 9))
        tutorial_instructions_iteration.pack()

        # Instructions pour l'axiome
        tutorial_instructions_axiom = tk.Label(tutorial_window, text="2. Axiome: Entrez l'axiome initial pour la chaîne L-System.", font=("Arial", 9))
        tutorial_instructions_axiom.pack()

        # Instructions pour les règles
        tutorial_instructions_rules = tk.Label(tutorial_window, text="3. Règles: Entrez les règles de remplacement pour chaque symbole de l'axiome.", font=("Arial", 9))
        tutorial_instructions_rules.pack()

        # Instructions pour la rotation et la longueur
        tutorial_instructions_rotationlongueur = tk.Label(tutorial_window, text="4. Rotation et Longueur: Entrez les valeurs pour la rotation et la longueur de la tortue.", font=("Arial", 9))
        tutorial_instructions_rotationlongueur.pack()

        # Instructions pour dessiner
        tutorial_instructions_draw = tk.Label(tutorial_window, text="5. Une fois que vous avez rempli les champs, cliquez sur les boutons situés en dessous des lettres A à E pour choisir ce qu'elles feront.\nPar exemple : avancer, tourner à gauche, sauvegarder..", font=("Arial", 9))
        tutorial_instructions_draw.pack()

        # Instructions pour générer
        tutorial_instructions_generate = tk.Label(tutorial_window, text="6. Cliquez sur le bouton 'Envoyer' pour créer la chaîne L-System et dessiner le résultat.", font=("Arial", 9))
        tutorial_instructions_generate.pack()

        # Séparateur
        separator = tk.Label(tutorial_window, text="")
        separator.pack()

        # Choisir un L-System prédéfini
        tutorial_predefined = tk.Label(tutorial_window, text="Vous pouvez également choisir un L-System prédéfini en cliquant sur le bouton None\net en en sélectionnant un parmi ceux proposés.", font=("Arial", 12))
        tutorial_predefined.pack()

        # Séparateur
        separator = tk.Label(tutorial_window, text="")
        separator.pack()

        # Fonction pour fermer la fenêtre de tutoriel
        def close_tutorial():
            global tutorial_open

            # Fermer la fenêtre de tutoriel
            tutorial_window.destroy()

            # Mettre à jour l'état de la fenêtre de tutoriel
            tutorial_open = False

        # Définir la fonction de fermeture de la fenêtre de tutoriel lorsqu'on clique sur la croix
        tutorial_window.protocol("WM_DELETE_WINDOW", close_tutorial)

        # Création d'un bouton pour fermer la fenêtre
        button_close = tk.Button(tutorial_window, text="Fermer", command=close_tutorial)
        button_close.pack()

        # Séparateur
        separator = tk.Label(tutorial_window, text="")
        separator.pack()

        # Exécuter la fenêtre de tutoriel
        tutorial_window.mainloop()
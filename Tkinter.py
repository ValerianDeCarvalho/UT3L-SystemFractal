import tkinter

def recupererValeur(iter,axio,dico,window):
    # Récupérer les valeurs des champs d'entrée
    global iteration
    global axiome
    global dictionnaire

    # Récupérer et convertir l'itération en entier avec stringToInt
    iteration = stringToInt(iter.get())

    # Récupérer l'axiome
    axiome = axio.get()

    # Boucle de validation de l'axiome
    while not testAxiome(axiome):
        # Afficher un message d'erreur si l'axiome n'est pas valide
        tkinter.messagebox.showerror("Erreur", "L'axiome ne peut contenir que les éléments 'A', 'B' ou 'C'.")
        # Réinitialiser l'entrée de l'axiome
        axio.delete(0, 'end')
        axiome.insert(0,"A")
        # Attendre que l'utilisateur corrige l'axiome en fermant la fenêtre modale
        window.wait_window()

    # Récupérer et convertir le dictionnaire en dictionnaire avec stringToDico
    dictionnaire = stringToDico(dico.get())

    # Boucle de validation du dictionnaire
    while not testDictionnaire(dictionnaire):
        # Afficher un message d'erreur si le dictionnaire n'est pas valide
        tkinter.messagebox.showerror("Erreur", "Le dictionnaire ne peut contenir que les éléments 'A', 'B' ou 'C'.")
        # Réinitialiser l'entrée du dictionnaire
        dico.delete(0, 'end')
        dico.insert(0, '"A":"ABC","B":"ABC","C":"ABC"')
        # Attendre que l'utilisateur corrige le dictionnaire en fermant la fenêtre modale
        window.wait_window()

    # Fermer la fenêtre
    window.destroy()

def stringToDico(string):
    # Ajouter des accolades pour créer une expression de dictionnaire valide
    stringtmp = "{" + string + "}"
    # Ajouter des accolades pour créer une expression de dictionnaire valide
    return eval (stringtmp) 

def stringToInt(string):
    return int (string)

def testAxiome(axiome):
    # Parcourir chaque caractère de l'axiome
    for char in axiome:
        # Vérifier si le caractère est parmi 'A', 'B' ou 'C'
        if char not in 'ABC':
            return False
    # L'axiome est valide s'il ne contient que des 'A', 'B' ou 'C'
    return True

def testDictionnaire(dictionnaire):
    for key, value in dictionnaire.items():
        if not (set(key) <= {'A', 'B', 'C'} and set(value) <= {'A', 'B', 'C'}):
            return False
    return True

def window():
    # Création de la fenêtre principale
    window = tkinter.Tk()
    window.title("lSystem")

    # Affichage du texte pour l'itération
    labeliteration = tkinter.Label(window, text="Entrez le nombre d'itérations :")
    labeliteration.pack()

    # Entrée pour l'itération
    iteration = tkinter.Entry(window, width=75)
    iteration.insert(0,"8")
    iteration.pack()

    # Affichage du texte pour l'axiome
    labelaxiome = tkinter.Label(window, text="Entrez l'axiome :")
    labelaxiome.pack()

    # Entrée pour l'axiome
    axiome = tkinter.Entry(window, width=75)
    axiome.insert(0,"A")
    axiome.pack()

    # Affichage du texte pour le dictionnaire
    labeldictionnaire = tkinter.Label(window, text="Entrez le dictionnaire :")
    labeldictionnaire.pack()

    # Entrée pour le dictionnaire
    dico = tkinter.Entry(window, width=75)
    dico.insert(0,'"A":"ABC","B":"ABC","C":"ABC"')
    dico.pack()

    # Bouton pour déclencher la récupération de la valeur
    bouton_recuperer = tkinter.Button(window, text="Envoyer", command=lambda: recupererValeur(iteration,axiome,dico,window))
    bouton_recuperer.pack()

    # Démarrer la boucle principale de la fenêtre
    window.mainloop()
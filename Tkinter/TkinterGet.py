import tkinter

valA=0
valB=1
valC=2
valD=3
valE=4

# Récupérer la valeur de A
def ValueA(x):
    global valA
    valA = x

# Récupérer la valeur de B
def ValueB(x):
    global valB
    valB = x

# Récupérer la valeur de C
def ValueC(x):
    global valC
    valC = x

# Récupérer la valeur de D
def ValueD(x):
    global valD
    valD = x

# Récupérer la valeur de E
def ValueE(x):
    global valE
    valE = x

def testAxiome(axiome):
    # Parcourir chaque caractère de l'axiome
    for char in axiome:
        # Vérifier si le caractère est parmi 'A', 'B', 'C', 'D' ou 'E'
        if char not in 'ABCDE':
            return False
    # L'axiome est valide s'il ne contient que des 'A', 'B', 'C', 'D' ou 'E'
    return True

def recupererValeur(iter,axio,tup,window):
    # Récupérer les valeurs des champs
    global iteration
    global axiome
    global rules
    # Récupérer et convertir l'itération en entier avec stringToInt
    iteration = stringToInt(iter.get())
    # Récupérer l'axiome
    axiome = axio.get()
    # Récupérer les règles et les convertir en tuple avec stringToTuple
    rules = stringToTuple(tup.get())
    # Boucle de validation de l'axiome
    while not testAxiome(axiome):
        # Afficher un message d'erreur si l'axiome n'est pas valide
        tkinter.messagebox.showerror("Erreur", "L'axiome ne peut contenir que les éléments 'A', 'B', 'C', 'D' ou 'E'.")
        # Réinitialiser l'entrée de l'axiome
        axio.delete(0, 'end')
        axiome.insert(0,"A")
        # Attendre que l'utilisateur corrige l'axiome en fermant la fenêtre modale
        window.wait_window()
    # Fermer la fenêtre
    window.destroy()

# Convertir une chaîne en entier
def stringToInt(string):
    return int(string)

# Convertir une chaîne en tuple
def stringToTuple(string):
    return tuple(string.split(','))
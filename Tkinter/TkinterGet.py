import tkinter

valA=0
valB=0
valC=0
valD=0
valE=0

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

def testRule(rule):
    # Parcourir chaque caractère de la règle
    for char in rule:
        # Vérifier si le caractère est parmi 'A', 'B', 'C', 'D' ou 'E'
        if char not in 'ABCDE':
            return False
    # La règle est valide si elle ne contient que des 'A', 'B', 'C', 'D' ou 'E'
    return True

def recupererValeur(iter,axio,tup,window):
    # Récupérer les valeurs des champs
    global iteration
    global axiome
    global rule

    # Récupérer et convertir l'itération en entier avec stringToInt
    iteration = stringToIt(iter.get())

    # Récupérer l'axiome
    axiome = axio.get()
    
    # Récupérer les règles et les convertir en tuple avec stringToTuple
    rule = stringToRule(tup.get())

    # Boucle de validation de l'axiome
    while not testAxiome(axiome):
        # Afficher un message d'erreur si l'axiome n'est pas valide
        tkinter.messagebox.showerror("Erreur", "L'axiome ne peut contenir que les éléments 'A', 'B', 'C', 'D' ou 'E'.")
        # Réinitialiser l'entrée de l'axiome
        axiome.delete(0, 'end')
        axiome.insert(0,"A")
        # Attendre que l'utilisateur corrige l'axiome en fermant la fenêtre modale
        window.wait_window()

    # Fermer la fenêtre
    window.destroy()

# Convertir une chaîne en entier
def stringToIt(string):
    return int(string)

# Convertir une chaîne en tuple
def stringToRule(string):
    # Supprimer les espaces
    string = string.replace(" ", "")
    # Diviser la chaîne en une liste de paires
    pairs = string.split(";")
    # Diviser chaque paire en deux éléments et créer un tuple
    result = [(pair.split(",")[0], pair.split(",")[1]) for pair in pairs]
    return result
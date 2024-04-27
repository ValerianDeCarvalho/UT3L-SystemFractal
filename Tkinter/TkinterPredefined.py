from Tkinter import TkinterGet

def none(axiom, rules, iteration, length, rotation):
    # Efface le champ d'entrée de l'axiome et insère la valeur par défaut.
    axiom.delete(0, 'end')
    axiom.insert(0, "A")
    # Efface le champ d'entrée des règles et insère la valeur par défaut.
    rules.delete(0, 'end')
    rules.insert(0, "A,B")
    # Efface le champ d'entrée du nombre d'itérations et insère la valeur par défaut.
    iteration.delete(0, 'end')
    iteration.insert(0, "4")
    # Efface le champ d'entrée de la longueur et insère la valeur par défaut.
    length.delete(0, 'end')
    length.insert(0, "10")
    # Efface le champ d'entrée de la rotation et insère la valeur par défaut.
    rotation.delete(0, 'end')
    rotation.insert(0, "25")
    # Définit des variables pour chaque lettre de l'axiome.
    TkinterGet.valA = 0
    TkinterGet.valB = 0
    TkinterGet.valC = 0
    TkinterGet.valD = 0
    TkinterGet.valE = 0

# Cette fonction initialise les champs d'entrée pour générer un arbre.
def arbre(axiom, rules, iteration, length, rotation):
    # Efface le champ d'entrée de l'axiome et insère la valeur par défaut.
    axiom.delete(0, 'end')
    axiom.insert(0, "A")
    # Efface le champ d'entrée des règles et insère la valeur par défaut.
    rules.delete(0, 'end')
    rules.insert(0, 'A,AACDCABABAEBDBACACAE')
    # Efface le champ d'entrée du nombre d'itérations et insère la valeur par défaut.
    iteration.delete(0, 'end')
    iteration.insert(0, "4")
    # Efface le champ d'entrée de la longueur et insère la valeur par défaut.
    length.delete(0, 'end')
    length.insert(0, "10")
    # Efface le champ d'entrée de la rotation et insère la valeur par défaut.
    rotation.delete(0, 'end')
    rotation.insert(0, "25")
    # Définit des variables pour chaque lettre de l'axiome.
    TkinterGet.valA = 0
    TkinterGet.valB = 1
    TkinterGet.valC = 2
    TkinterGet.valD = 3
    TkinterGet.valE = 4

# Cette fonction initialise les champs d'entrée pour générer un flocon de Koch.
def flocon(axiom, rules, iteration, length, rotation):    
    # Efface le champ d'entrée de l'axiome et insère la valeur par défaut.
    axiom.delete(0, 'end')
    axiom.insert(0, "ACCACCA")
    # Efface le champ d'entrée des règles et insère la valeur par défaut.
    rules.delete(0, 'end')
    rules.insert(0, 'A,ABACCABA')
    # Efface le champ d'entrée du nombre d'itérations et insère la valeur par défaut.
    iteration.delete(0, 'end')
    iteration.insert(0, "3")
    # Efface le champ d'entrée de la longueur et insère la valeur par défaut.
    length.delete(0, 'end')
    length.insert(0, "10")
    # Efface le champ d'entrée de la rotation et insère la valeur par défaut.
    rotation.delete(0, 'end')
    rotation.insert(0, "60")
    # Définit des variables pour chaque lettre de l'axiome.
    TkinterGet.valA = 0
    TkinterGet.valB = 1
    TkinterGet.valC = 2
    TkinterGet.valD = 3
    TkinterGet.valE = 4

def fleur(axiom, rules, iteration, length, rotation):
    # Efface le champ d'entrée de l'axiome et insère la valeur par défaut.
    axiom.delete(0, 'end')
    axiom.insert(0, "DDDDDDDDDDB")
    # Efface le champ d'entrée des règles et insère la valeur par défaut.
    rules.delete(0, 'end')
    rules.insert(0, 'A,DDDCDCCDCDDDCCD;B,DACDAEEDAB')
    # Efface le champ d'entrée du nombre d'itérations et insère la valeur par défaut.
    iteration.delete(0, 'end')
    iteration.insert(0, "10")
    # Efface le champ d'entrée de la longueur et insère la valeur par défaut.
    length.delete(0, 'end')
    length.insert(0, "10")
    # Efface le champ d'entrée de la rotation et insère la valeur par défaut.
    rotation.delete(0, 'end')
    rotation.insert(0, "45")
    # Définit des variables pour chaque lettre de l'axiome.
    TkinterGet.valA = 0
    TkinterGet.valB = 1
    TkinterGet.valC = 2
    TkinterGet.valD = 0
    TkinterGet.valE = 1
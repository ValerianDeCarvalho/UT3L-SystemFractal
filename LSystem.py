# Génère une séquence L-System en appliquant les règles un certain nombre d'itérations.
def lSystemCreate(ax,ru,it):
    # Boucle pour appliquer les règles itérativement
    while it !=0 :
        # Appliquer les règles sur l'axiome actuel
        ax = lSystemRules(ax,ru)
        # Décrémenter le compteur d'itérations
        it -= 1
    # Retourner la séquence L-System générée
    return ax

# Applique les règles de remplacement du L-System à l'axiome donné.
def lSystemRules (ax,ru):
    # Initialisation de la nouvelle séquence vide
    new = ''
    # Parcours de chaque caractère dans l'axiome actuel
    for caractere in ax:
        # Vérifier si le caractère est défini dans les règles
        if caractere in ru:
            # Ajouter à la nouvelle séquence la valeur associée à la clé dans les règles
            new += ru[caractere]
    # Retourner la nouvelle séquence résultante après l'application des règles
    return new
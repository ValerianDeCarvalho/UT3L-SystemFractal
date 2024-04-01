def lSystemCreate(ax, ru, it):
    # Répète l'opération 'it' fois
    for i in range(it):
        # Remplace les caractères spécifiés dans 'ru' dans la chaîne 'ax'
        ax = ax.replace(*ru)
    # Retourne la chaîne 'ax' modifiée
    return ax
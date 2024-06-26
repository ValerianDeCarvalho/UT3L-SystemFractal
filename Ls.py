# La fonction prend trois paramètres : l'axiome de départ, les règles de remplacement, et le nombre d'itérations.
def lSystemCreate(axiome, rule, iteration):
    # Répète l'opération pour chaque itération
    for _ in range(iteration):
        # Pour chaque itération, une nouvelle chaîne temporaire est créée pour stocker le résultat de l'itération actuelle.
        temp = ''
        # Parcourt chaque symbole de l'axiome actuel.
        for j in range(len(axiome)):
            # On a un dictionnaire Parcourt chaque règle de remplacement.
            v=rule.get(axiome[j])
            if v!=None:
                temp += v
            else: # Si aucun remplacement n'est trouvé pour le symbole, il est simplement ajouté à la chaîne temporaire.
                temp += axiome[j]
        # La nouvelle axiome est mise à jour avec la chaîne temporaire pour la prochaine itération.
        axiome = temp

    # Retourne la chaîne axiome modifiée après toutes les itérations.
    return axiome
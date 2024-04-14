def lSystemCreate(axiome, règle, itération):
    
    # Répète l'opération pour chaque itération
    for _ in range(itération):
        temp = ''
        for j in range(len(axiome)):
            for k in range(len(règle)):
                if axiome[j] == règle[k][0]:
                    temp += règle[k][1]
                    break
            else:
                temp += axiome[j]
        axiome = temp

    # Retourne la chaîne axiome modifiée
    return axiome
import utils
import LsConfig


# On va verifier que chaque lettre de l'axiome est bien present
def test_axiom_in_rule(ax,rule):
     errs=[]
     warns=[]
     for c in ax:
         if not c in LsConfig.permit_ax_elmts :
             utils.appendIfNotPresent(warns,"Element "+c+" De l'axiome pas permis dans la grammaire")
         if rule.get(c)==None:
             utils.appendIfNotPresent(warns,"Element "+c+" De l'axiome sans regle d'iteration")
     return errs,warns

# Renvoi un dictionaire avec les commandes graphiques associées à chaque lettre
# Si erreur
def stringToGraphicRule(string):
    result={}
    errs=[]
    # Supprimer les differents types d'espaces
    string = string.replace(" ", "")
    string = string.replace("\r", "")
    string = string.replace("\n", "")
    # Diviser la chaîne en une liste de paires
    pairs = string.split(";")
    # Diviser chaque paire en deux éléments et créer un dictionnaire
    for pair in pairs:
        cmdValue=pair.split("=") # on split entre la commande et la valeur
        if result.get(cmdValue[0])==None:
            result[cmdValue[0]]=cmdValue[1].split(":")
            if not result[cmdValue[0]][0] in LsConfig.predefined_options: # Erreur ne devrait pas arriver car elle vient du fichier csv qui a du etre enregistré correctement, mais au cas ou on l'utiliserait pour un text brut on gere l'erreur
                utils.appendIfNotPresent(errs,"Commande graphique "+result[cmdValue[0]][0]+" inconnue")
        else: # Erreur ne devrait pas arriver car elle vient du fichier csv qui a du etre enregistré correctement, mais au cas ou on l'utiliserait pour un text brut on gere l'erreur
            utils.appendIfNotPresent(errs,"Commande "+cmdValue[0]+" est dupliquee")
    return result,errs

# Convertir une chaîne en tuple dictionnaire
# une regle a le format 
# LettreCommande=SuiteDeLettre;
# LettreCommande=SuiteDeLettre
def stringToRule(string):
    errs=[] # liste d'erreurs retournées
    warns=[] # liste de warning retournées
    result={} # retourne un dictionaire
    # Supprimer les espaces
    string = string.replace(" ", "")
    string = string.replace("\r", "")
    string = string.replace("\n", "")
    # Diviser la chaîne en une liste de paires
    pairs = string.split(";")
    for i in range(len(pairs)) :
        if not pairs[i]:
            utils.appendIfNotPresent(errs,"Ligne vide avec ;")
    if not(errs):
        # Diviser chaque paire en deux éléments et créer un element de dictionaire
        for pair in pairs:
            split=pair.split("=")
            if len(split)==2:
                 cmd=split[0]
                 value=split[1]
                 if result.get(cmd)==None:
                     result[cmd] =value
                     if value=="":
                         utils.appendIfNotPresent(warns,"Valeur vide pour la commande "+cmd+" sans effet")
                 else:
                     utils.appendIfNotPresent(errs,"Regle "+cmd+" deja definie")
            else:
                 utils.appendIfNotPresent(errs,"Format de la ligne "+pair+" Incorrect")
    return result,errs,warns

#definition d'une classe pour stocker les regles graphiques
class GraphRule:
    def __init__(self,command,rot,len):
        self.command=command
        self.rot=rot
        self.len=len
# Contient des fonctions et utilitaires reutilisables

def testIfUInt(str): 
    return str.isdigit()

def testIfInt(str): # Besoin de recreer car isdigit ou isnumeric 
    if str[0] in ('-', '+'):
        return testIfUInt(str[1:])
    return testIfUInt(str)

def appendIfNotPresent(list,text):
    if not text in list:
        list.append(text)
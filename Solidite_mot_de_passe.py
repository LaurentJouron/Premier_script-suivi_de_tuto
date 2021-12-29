Mot_De_Passe = input("Veuillez saisir votre mot de passe: ")

# Nombre de caractères dans le mot de passe
def Caractere(Mot_De_Passe):
    return len(Mot_De_Passe)

# Nombre de caractères majuscules
def NbCMaj(Mot_De_Passe):
    return sum(map(str.isupper, Mot_De_Passe))

# Nombre de caractères minuscules
def NbCMin(Mot_De_Passe):
    return sum(map(str.islower, Mot_De_Passe))

# (Nombre de caractère non-Alphanumérique
def NbCAlpha(Mot_De_Passe):
    return sum(map(str.isalnum, Mot_De_Passe))

# Longueur de la plus grande séquence de lettre minuscule
Majuscule = NbCMaj(Mot_De_Passe)
Minuscule = NbCMin(Mot_De_Passe)
def LongMaj(Securite_Mot_De_Passe):
    Majuscule = 0
    Minuscule = 0
    while Majuscule < len(Securite_Mot_De_Passe):
        if Majuscule < len(Securite_Mot_De_Passe) < Minuscule:
            Majuscule += 1
        return Majuscule

# Longueur de la plus grande séquence de lettre majuscule
def LongMin(Securite_Mot_De_Passe):
    Majuscule = 0
    Minuscule = 0
    while Minuscule < len(Securite_Mot_De_Passe):
        if Minuscule < len(Securite_Mot_De_Passe) < Majuscule:
            Minuscule += 1
        return Minuscule

Caracteres = Caractere(Mot_De_Passe)
Non_Alphanumerique = NbCAlpha(Mot_De_Passe)
Sequence_Majuscule = LongMaj(Mot_De_Passe)
Sequence_Minuscule = LongMin(Mot_De_Passe)

def score():
    Caractere = Caracteres*4
    Majuscules = (Caracteres - Majuscule)*2
    Minuscules = (Caracteres - Minuscule)*3
    Non_AlphaNum = Non_Alphanumerique*5
    Seq_Minuscule = Sequence_Minuscule*2
    Seq_Majuscule = Sequence_Majuscule*3
    return Caractere + Majuscules + Minuscules + Non_AlphaNum - Seq_Minuscule - Seq_Majuscule

scores = score()
def resultat():
    if scores > 80:
        print("Très fort")
    elif scores < 40:
        print("Fort")
    elif scores < 20:
        print("Faible")
    elif scores > 0:
        print("Très faible")
resultat()
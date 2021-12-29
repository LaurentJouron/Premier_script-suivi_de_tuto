import random

NOMBRE_MIN = 1
NOMBRE_MAX = 20
NB_QUESTION = 10

def poser_question():
    a = random.randint(NOMBRE_MIN, NOMBRE_MAX)
    b = random.randint(NOMBRE_MIN, NOMBRE_MAX)
    o = random.randint(0, 2)
    operateur_str = "+"
    if o == 1:
        operateur_str = "*"
        if o == 2:
            operateur_str = "-"
    reponse_str = input(f"Calculez {a} {operateur_str} {b} = ")
    reponse_int = int(reponse_str)
    calcul = a+b
    if o == 1:
        calcul = a*b
    if o == 2:
        calcul = a-b
    if reponse_int == calcul:
        return True
    return False

nb_points = 0
for i in range(0, NB_QUESTION):
    print(f"Question n°{i+1} sur {NB_QUESTION}:")
    if poser_question():
        print("Réponse correct!")
        nb_points += 1
    else:
        print("Réponse incorrect!")
    print()
print(f"Votre note est de : {nb_points} / {NB_QUESTION}")

moyenne = int(NB_QUESTION/2)
if nb_points == NB_QUESTION:
    print("Excellent!")
elif nb_points == 0:
    print("Révisez vos maths!")
elif nb_points > moyenne:
    print("Pas mal!")
else:
    print("Peut mieux faire!")

Quitter = ""
while Quitter != "o":

    nombre1 = input("Saisissez un nombre : ")
    if nombre1.isdigit():
        nombre1 = int(nombre1)
        for i in range(11):
            print(str(i) + " x " + str(nombre1) + " = " + str(i * nombre1))
        Quitter = input("Voulez-vous quitter ? o/n ")
    else:
        print("Ce n'est pas un nombre ça!!! Entrez un nombre, s'il vous plait !!!")
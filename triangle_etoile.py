def triangle(nombre_De_Rang):
    hauteur = nombre_De_Rang
    nombre_D_Etoiles = 1
    nombre_D_Espaces = hauteur - 1
    for indice in range(hauteur):
        print(nombre_D_Espaces * " " + nombre_D_Etoiles * "*")
        nombre_D_Etoiles += 2
        nombre_D_Espaces -= 1
triangle(int(input("Saisir la hauteur du triange : ")))

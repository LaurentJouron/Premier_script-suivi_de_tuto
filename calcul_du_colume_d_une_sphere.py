from math import pi

def cube(rayon):
    return rayon**3

def VolumeSphere(rayon):
    return 4*pi*cube(rayon)/3

rayon = float(input("Saisir la valeur du rayon : "))
print("\nLe volume d'un sphère du rayon {0:.2f} est {1:.3f} ".format(rayon, VolumeSphere(rayon)))

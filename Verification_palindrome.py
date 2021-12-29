def palindrome(Ville):
    for i in range(len(Ville) // 2):
        if Ville[i] != Ville[-i - 1]:
            return False
    return True

Ville = input("Entrez le nom d'une ville : ")

if palindrome(Ville) == True:
    print("C'est un palindrome.")
else:
    print("Ce n'est pas un palindrome.")

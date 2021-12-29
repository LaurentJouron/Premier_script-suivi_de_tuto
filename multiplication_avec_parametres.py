def table(mul, born_Inf, born_Sup):
    while born_Inf <= born_Sup:
        print(born_Inf, "x", mul, "=", born_Inf * mul)
        born_Inf += 1


table(mul=int(input("Saisir le nombre multiplicateur: ")),
      born_Inf=int(input("Veuillez saisir le premier chiffre: ")),
      born_Sup=int(input("Veuillez saisir le second chiffre: ")))
def trad_binaire(nb):
    tab = [128, 64, 32, 16, 8, 4, 2, 1]
    binaire = [0] * 8
    res = []
    nb_modif = nb
    for i in range(len(tab)):
        if nb_modif - tab[i] >= 0:
            nb_modif = nb_modif - tab[i]
            res.append(tab[i])

            for j in range(len(res)):
                if res[j] in tab:
                    place = tab.index(res[j])
                    binaire[place] = 1
    print("La décomposition de", nb, "est", res)
    print(binaire)
    input("Appuyez sur ENTRER pour continuer...")


nb = ''
while ValueError or nb > 255 or nb < 0:
    try :
        nb = int(input("Choisir nombre entier compris entre 0 et 255 inclus : "))
        if nb <= 255 and nb >= 0:
            print("Le nombre choisi est", nb, ", ce nombre est valide.")
            trad_binaire(nb)
            break
        else :
            print("Le nombre", nb, "n\'est pas compris entre 0 et 255 inclus.")
    except ValueError:
        print("Chosir un entier ! ")


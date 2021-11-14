import time
time_duration = 1
def choix():
    un = "1) traduire base 2 en base 10"
    deux = "2) traduire base 10 en base 2"
    trois = "3) Quitter"
    print("Choisir un nombre entre 1 et 3 pour sélectionner une option")
    print(un)
    print(deux)
    print(trois)
    try:
        choixOption = int(input("Choix n° --> "))
        print(choixOption)
        if choixOption == 1:
            print("L'option choisie est :",un)
            selectionNombre(1)
        elif choixOption == 2:
            print("L'option choisie est :",deux)
            selectionNombre(2)
        elif choixOption == 3:
            print("L'option choisie est :",trois)
            print("Le programme a pris fin")
            exit
        else :
            print("L'option",choixOption,"n'existe pas")
            choix()
    except ValueError:
        print("Erreur, l'entrée saisie n'est pas un nombre")
        choix()

def selectionNombre(code):
    if code == 1:
        try :
            nb = int(input("Choisir nombre binaire à traduire en decimal ==> "))
            nb=str(nb)
            c=0
            for i in range(len(nb)):
                    if nb[i] !='0' and nb[i] != '1':
                        c = c + 1
            if c !=0:
                print("Erreur le nombre",nb," n'est pas binaire")
                selectionNombre(1)
            else:
                nb = int(nb)
                translateIntoDec(nb)
        except ValueError:
            print("Chosir un entier ! ")
            selectionNombre(1)
    if code == 2:
        try :
            nb = int(input("Choisir nombre entier à traduire en binaire ==> "))
            print("Le nombre choisi est", nb, ", ce nombre est valide.")
            translateIntoBin(nb)
        except ValueError:
            print("Chosir un entier ! ")
            selectionNombre(2)


def translateIntoBin(nb):
    a=1
    tabDec= []
    while a <= nb:
        res = a
        tabDec.insert(0,res)
        a=a*2
    print(tabDec)
    longueur = len(tabDec)
    binaire = [0] * longueur
    res = []
    nb_modif = nb
    for i in range(len(tabDec)):
        if nb_modif - tabDec[i] >= 0:
            nb_modif = nb_modif - tabDec[i]
            res.append(tabDec[i])
            for j in range(len(res)):
                if res[j] in tabDec:
                    place = tabDec.index(res[j])
                    binaire[place] = 1
    print("La décomposition de", nb, " en base 10 est", res)
    bina =''
    for elem in binaire:
        elem=str(elem)
        bina=bina+elem
    print(nb,"en base 2 est :",bina)
    print("")
    time.sleep(time_duration)
    sortie()

def translateIntoDec(nb):
    a=1
    b = 1
    tabDec= []
    nbStr = str(nb)
    long = len(nbStr)
    while b <= long:
        res = a
        tabDec.insert(0,res)
        a=a*2
        b=b+1
    nbFin=0
    for i in range(long):
        if nbStr[i] == '1':
            nbFin=nbFin+tabDec[i]
    print(nb,"en base 10 est :",nbFin)
    time.sleep(time_duration)
    print("")
    sortie()


def sortie():
    YorN = input("Voulez-vous convertir un nouveau nombre ? Saisir \"O\" pour Oui ou \"N\" pour Non ==> ")
    if YorN == 'O' or YorN == 'o':
        choix()
    elif YorN =='N'or YorN == 'n':
        print("La sélection est Non, le programme prend fin")
    else:
        print("Erreur de saisie")
        sortie()

choix()

def interet():


    try:
        somme = float(input("Capital initial?"))
        annees = int(input("Nombre d'annees"))
        taux = float(input("Taux interet en %"))

        if somme < 0 or annees < 0 or taux <0:
            raise ValueError()
        else:
            total = somme* (1 + taux / 100)**annees
    except ValueError as erreur:
        print("La valeur n'est pas valise \n")
        print(erreur)
    else:
        return("Vous allez recevoir {:.2f} euros".format(total))


interet()

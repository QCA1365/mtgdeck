print("1. Consulter l'inventaire --> Code et quantité seulement")
print("2. Ajouter une carte à l'inventaire")
print("3. Retirer une carte de l'inventaire")
action = input("Que veux-tu faire? ")
if action == '1':
    print("1. Chercher une carte par numero")
    print("2. Afficher l'ensemble des cartes de l'inventaire (Au moins une possédée")
    data = input("Que dois-je chercher? ")
    if data == "1":
        card = input("Quel est le numero de la carte? (série + chiffre --> AAA123) ")
        CardFormat = (card[:3] + '/' + card[3:])
        CardSet = card[:3]
        CardNumber = card[3:]
        file = open(("inventory/"+CardSet.upper()+".txt"), "r")
        lines = file.readlines()
        print(lines[int(CardNumber)-1])

    elif data == "2":
        file = open("inventory/sets.txt", "r")
        lines = file.readlines()
        sets = []
        ListeSets = []
        for i in lines:
            name, code = i.split(',')
            CardSet = open(("inventory/"+name+".txt"),"r")
            CardList = CardSet.readlines()
            for Cards in CardList:
                CardsClean = Cards.replace("\n","")
                if int(CardsClean[7:]) >= 1:
                    print(CardsClean)
            CardSet.close()
        file.close()
        
        

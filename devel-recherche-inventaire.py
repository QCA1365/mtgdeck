while True:
    print("1. Consulter l'inventaire --> Code et quantité seulement")
    print("2. Ajouter / Retirer une carte à l'inventaire")
    action = input("Que veux-tu faire? ")
    if action == '1':
        print("1. Chercher une carte par numero")
        print("2. Afficher l'ensemble des cartes de l'inventaire (Au moins une possédée")
        data = input("Que dois-je chercher? ")
        if data == "1":
            card = input("Quel est le numero de la carte? (série + chiffre --> AAA123) ")
            CardSet = card[:3]
            CardNumber = card[3:]
            file = open(("inventory/"+CardSet.upper()+".txt"), "r")
            lines = file.readlines()
            print(lines[int(CardNumber)-1])

        elif data == "2":
            file = open("inventory/.sets.txt", "r")
            lines = file.readlines()
            sets = []
            ListeSets = []
            PrintedCards = 0
            for i in lines:
                name, code = i.split(',')
                CardSet = open(("inventory/"+name+".txt"),"r")
                CardList = CardSet.readlines()
                for Cards in CardList:
                    CardsClean = Cards.replace("\n","")
                    if len(CardsClean) == 14:
                        if int(CardsClean[13:]) >= 1:
                            print(CardsClean)
                            PrintedCards = PrintedCards+1
                    elif len(CardsClean) >= 15:
                        print(CardsClean)
                        PrintedCards = PrintedCards+1
                CardSet.close()
            file.close()
            if PrintedCards == 0:
                print("Aucune carte dans l'inventaire\n")

    elif action == '2':
        CardID = input("Quel est le numero de la carte? (série + chiffre --> AAA123) ")
        CardSet = CardID[:3]
        file = open("inventory/"+CardSet+".txt","r")
        AllRawCards = file.readlines()
        AllCards = []
        for RawCard in AllRawCards:
            WholeCards = []
            WholeCards = RawCard.replace("\n","").split(" ---> ")
            AllCards.append(WholeCards)
        file.close()
        card = AllCards[int(CardID[-3:])-1]
        print("Ceci est ta carte:")
        print(card)
        while True:
            confirmation = input("Est-ce bien ta carte? (y/n) ")
            if confirmation == "y":
                QtyToAdd = int(input("Combien à ajouter / retirer? (Pour retirer, ajouter un moins devant) "))
                QtyInInventory = int(card[1])
                NewQty = QtyToAdd + QtyInInventory
                card[1] = NewQty
                break
            elif confirmation == "n":
                break
            else:
                print("Cette entrée n'est pas valide, veuillez réessayer")
        
        AllCards[int(CardID[-3:])-1] = card
        file = open("inventory/"+CardSet+".txt","w")
        for x in AllCards:
            FormattedCard =  (x[0] + " ---> " + str(x[1]) + "\n")
            file.write(FormattedCard)
        file.close()
            

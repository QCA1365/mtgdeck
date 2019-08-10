import os

def RemplirSets(filename, ListeSets):
    file = open(filename, "r")
    lines = file.readlines()
    sets = []
    for i in lines:
        name, code = i.split(',')
        sets.append(name)
        sets.append(code.replace("\n", ""))
        ListeSets.append(sets)
        sets = []
    file.close()

def RemplirCartes(nomFichier, liste):
    fichier = open(nomFichier, "r")
    lines = fichier.readlines()
    card = []
    for i in lines:
        if len(i.split('"')) == 5:
            code, rarity, name, mana, category = i.split('"')
        elif len(i.split('"')) == 6:
            code, rarity, name, mana, category, strenght = i.split('"')
        card.append(code)
        card.append(rarity)
        card.append(name)
        card.append(mana)
        card.append(category.replace("\n", ""))
        if len(i.split('"')) == 6:
            card.append(strenght.replace("\n", ""))
        liste.append(card)
        card = []
    fichier.close()

def ColorTest(ManaCost):
    color1 = ManaCost[3].replace('B',' Black')
    color2 = color1.replace('U',' Blue')
    color3 = color2.replace('W',' White')
    color4 = color3.replace('R',' Red')
    color5 = color4.replace('G',' Green')
    return(color5)

def namesearch(deck, names):
    cards = []
    for x in deck:
        if names in x[2].split(' '):
           cards.append(x)
    for x in deck:
        if names in x[2].split("'"):
            cards.append(x)
    return cards

def ManaCalc(deck,worth):
    for x in deck:
        card = x
        manaColorless1 = x[3].replace('B','')
        manaColorless2 = manaColorless1.replace('U','')
        manaColorless3 = manaColorless2.replace('W','')
        manaColorless4 = manaColorless3.replace('G','')
        manaColorless5 = manaColorless4.replace('R','')
        OperationManas = manaColorless5.split(' ')
        if len(OperationManas) == 1:
            if OperationManas[0][:1] == 'X':
                ManaValue = 0
            elif OperationManas[0].isdigit() == True:
                ManaValue = int(OperationManas[0])
        elif len(OperationManas) == 2:
            if OperationManas[0].isdigit() == True and OperationManas[1].isdigit() == True:
                ManaValue = int(OperationManas[0]) + int(OperationManas[1])
            elif OperationManas[0] == 'X':
                ManaValue = 0 + int(OperationManas[1])
        card[3] = str(ManaValue)
        if card[3] == worth:
            print(card)
        elif OperationManas[0] == "X":
            if len(OperationManas) >= 2:
                if OperationManas[1] <= worth:
                    print(card)
            else:
                print(card)

###============== Main Program ==============###
os.system("python3 sets/setparser.py")

sets = []
RemplirSets("sets/TXT-SetFiles/sets.txt", sets)

while True:
    print("\nBienvenue dans l'index des cartes legales de Magic: The Gathering\n")
    print("1: Acces a l'inventaire")
    print("2: Chercher de l'information sur une carte")
    action = input("Que puis-je faire pour toi? ")
    if action == "1":
        print("\n1. Consulter l'inventaire --> Code et quantité seulement")
        print("2. Ajouter / Retirer une carte à l'inventaire")
        action = input("Que veux-tu faire? ")
        if action == '1':
            print("\n1. Chercher une carte par numero")
            print("2. Afficher l'ensemble des cartes de l'inventaire (Au moins une possédée")
            data = input("Que dois-je chercher? ")
            if data == "1":
                card = input("\nQuel est le numero de la carte? (série + chiffre --> AAA123) ")
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
            file = open("inventory/"+CardSet+".txt","w+")
            for x in AllCards:
                FormattedCard =  (x[0] + " ---> " + str(x[1]) + "\n")
                file.write(FormattedCard)
            file.close()

    
    elif action == "2":
        for x in range(len(sets)):
            print(sets[x][0] + " , " + sets[x][1])
        Deckname = input("Set? ")
        deck = []
        RemplirCartes(("sets/TXT-SetFiles/" +Deckname.upper()+ ".txt"), deck)
        print('\n1. Par numero\n2. Par rarete\n3. Par nom (Sensible a la casse)\n4. Par cout en manas\n5. Par type ')
        information = input('Comment souhaite-tu chercher ta carte? ')
        if information == '1':
            number = input('Quel est le numero de la carte? ')
            card_preliminary = deck[int(number)-1]
            card = card_preliminary
            card[3] = ColorTest(card)
            print("")
            print(card)

        elif information == '2':
            print("\n1. Common\n2. Uncommon\n3. Rare\n4. Mythic")
            scarcity = input('Quelle est la rareté de la carte? ')
            if scarcity == '1':
                ScarcityLetter = 'C'
            elif scarcity == '2':
                ScarcityLetter = 'U'
            elif scarcity == '3':
                ScarcityLetter = 'R'
            elif scarcity == '4':
                ScarcityLetter = 'M'
            for x in deck:
                if ScarcityLetter in x[1]:
                    card = x
                    x[3] = ColorTest(card)
                    print(card)
                
        elif information == '3':                                #Could be modified for keyword search 20190810@2109Z Esteban Carrillo
            names = input('Quel est le nom de la carte? ')
            card = namesearch(deck, names)
            for x in card:
                card = x
                card[3] = ColorTest(card)
                print(card)
    

        elif information == '4':
            print('1. Cout brut en manas (i.e 6 manas)')
            print('2. Cout detaille (i.e 3 + 2 Bleus)')
            quality = input("Comment veux-tu entrer tes manas? ")
            if quality == '1':
                quantity = input("Combien de manas? ")
                ManaCalc(deck,quantity)
            

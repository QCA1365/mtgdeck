sets = []

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
            code, rarity, name, mana, category,strenght = i.split('"')
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
    color2 = color1.replace('C',' Blue')
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
        manaColorless2 = manaColorless1.replace('C','')
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
sets = []

RemplirSets("sets/sets.txt", sets)

while True:
    print("\nBienvenue dans l'index des cartes legales de Magic: The Gathering\n")
    print("1: Acces a l'inventaire")
    print("2: Chercher de l'information sur une carte")
    action = input("Que puis-je faire pour toi? ")
    if action == "1":
        print("\nCette fonctionnalite n'est pas encore activee!")
    if action == "2":
        while True:
            print("\n1. " + sets[0][0])
            print("2. " + sets[1][0])
            print("3. " + sets[2][0])
            print("4. " + sets[3][0])
            print("5. " + sets[4][0])
            print("6. " + sets[5][0])
            print("7. " + sets[6][0])
            print("8. " + sets[7][0])
            Deckname = input("Set? ")
            if Deckname == '8':
                print("Cette serie n'est pas encore disponible, veuillez faire un autre choix")
            else:
                break
                      
        Database = sets[int(Deckname)-1][1]
        deck = []
        RemplirCartes(("sets/" +Database+ ".txt"), deck)
        print('\n1. Par numero\n2. Par rarete\n3. Par nom (Sensible a la casse)\n4. Par cout en manas\n5. Par type ')
        information = input('Comment souhaite-tu chercher ta carte?')
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
                
        elif information == '3':
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
            

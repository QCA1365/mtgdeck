def getcard(CardNumber):
    #CardSet = CardNumber[:3]
    CardSet = "testfile"
    file = open(CardSet+".txt","r")
    AllRawCards = file.readlines()
    AllCards = []
    for RawCard in AllRawCards:
        WholeCards = []
        WholeCards = RawCard.replace("\n","").split(" ---> ")
        AllCards.append(WholeCards)
    file.close()
    card = AllCards[int(CardNumber[-3:])-1]
    print("Ceci est ta carte:")
    print(card)
    while True:
        confirmation = input("Est-ce bien ta carte? (y/n) ")
        if confirmation == "y":
            QtyToAdd = int(input("Combien à ajouter? "))
            QtyInInventory = int(card[1])
            NewQty = QtyToAdd + QtyInInventory
            card[1] = NewQty
            break
        elif confirmation == "n":
            break
        else:
            print("Cette entrée n'est pas valide, veuillez réessayer")
    
    AllCards[int(CardNumber[-3:])-1] = card
    file = open(CardSet+".txt","w")
    for x in AllCards:
        FormattedCard =  (x[0] + " ---> " + str(x[1]) + "\n")
        file.write(FormattedCard)
    file.close()
    

CardID = "XLN004"
getcard(CardID)

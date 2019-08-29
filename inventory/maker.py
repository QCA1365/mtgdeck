file = open("sets/TXT-SetFiles/sets.txt", "r")
lines = file.readlines()
SetList = []
for mtgset in lines:
    mtgset = mtgset.replace('\n', '')
    SetList.append(mtgset)

### Folder Creation for New Sets ###
for CardSet in SetList:
    CardSet = CardSet.split(',')
    try:
        f = open(('inventory/' + CardSet[1])+'.txt','x')
        for x in range(1,int(CardSet[2])+1):
            if x <= 9:
                f.write(CardSet[1]+"/00"+str(x)+" ---> 0\n")
            elif x <= 99:
                f.write(CardSet[1]+"/0"+str(x)+" ---> 0\n")
            elif x <= 999:
                f.write(CardSet[1]+"/"+str(x)+" ---> 0\n")
        f.close()

    except FileExistsError:
        pass

print('maker.py is done!')

file = open("sets.txt", "r")
lines = file.readlines()
sets = []
ListeSets = []
for i in lines:
    name, code = i.split(',')
    sets.append(name)
    sets.append(code.replace("\n", ""))
    ListeSets.append(sets)
    sets = []
file.close()

### Folder Creation for New Sets ###

for CardSets in ListeSets: 
    try:
        f = open((CardSets[0])+'.txt','x')
        for x in range(1,int(CardSets[1])+1):
            if x <= 9:
                f.write(CardSets[0]+"/00"+str(x)+",\n")
            elif x <= 99:
                f.write(CardSets[0]+"/0"+str(x)+",\n")
            elif x <= 999:
                f.write(CardSets[0]+"/"+str(x)+",\n")
        f.close()

    except FileExistsError:
        pass

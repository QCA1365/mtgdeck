# Beginning of imports

import platform
import os
import glob
import json

# End of imports

<<<<<<< HEAD
<<<<<<< HEAD
sys = platform.system()
print(os.getcwd())

def SetFileCreator(sys):
=======
def SetFileCreator(files):
>>>>>>> origin/devel
=======
def SetFileCreator(files):
>>>>>>> origin/devel
	setList = []
	if sys == "Linux":
		with open("List/SetList.json","r") as SetData:
			data = json.load(SetData)
	elif sys == "Windows":
		with open("List/SetList.json","r") as SetData:
			data = json.load(SetData)
	for Set in data:
		CompleteSet = Set["name"] + "," + Set["code"] + "," + str(Set["totalSetSize"])
		setList.append(CompleteSet)
	SetData.close()
<<<<<<< HEAD
<<<<<<< HEAD
	if sys == "Linux":
		with open("../TXT-SetFiles/sets.txt", "w+") as AllSetsFile:	#sets.txt is required by repertoire.py 09082019@0046Z Esteban Carrillo -- TO BE ADDED IN DOCUMENTATION
			for setInfo in setList:
				AllSetsFile.write(setInfo + "\n")
	elif sys == "Windows":
		with open("../TXT-SetFiles/sets.txt", "w+") as AllSetsFile:	#sets.txt is required by repertoire.py 09082019@0046Z Esteban Carrillo -- TO BE ADDED IN DOCUMENTATION
			for setInfo in setList:
				AllSetsFile.write(setInfo + "\n")
	AllSetsFile.close()	
=======
=======
>>>>>>> origin/devel
	with open("../TXT-SetFiles/sets.txt", "w+") as AllSetsFile:	#sets/TXT-SetFiles/sets.txt is required by repertoire.py 09082019@0046Z Esteban Carrillo -- TO BE ADDED IN DOCUMENTATION
		for setInfo in setList:
			AllSetsFile.write(setInfo + "\n")
		AllSetsFile.close()	
>>>>>>> origin/devel

def rarity(cards):
	if cards["rarity"] == "common":
		return "C"
	elif cards["rarity"] == "uncommon":
		return "U"
	elif cards["rarity"] == "rare":
		return "R"
	elif cards["rarity"] == "mythic":
		return "M"

def manaCost(cards):
	try:
		raw_manas = cards["manaCost"]
		prepared_manas = raw_manas[1:]
		clean_manas = prepared_manas.replace("}","")
		cleaner_manas = clean_manas.split("{")
		for x in range(0,len(cleaner_manas)):
			if cleaner_manas[x].isdigit() == False and cleaner_manas[x] != "X":
				cleaner_manas[x] = "1" + cleaner_manas[x]
		for x in range(len(cleaner_manas)):
			try:
				cleaner_manas[x][1] == cleaner_manas[x+1][1]
				if cleaner_manas[x][1] == cleaner_manas[x+1][1]:
					mana_number = (str(int(cleaner_manas[x][0]) + int(cleaner_manas[x+1][0])))
					del cleaner_manas[x+1]
					cleaner_manas[x] = mana_number + cleaner_manas[x][1]
					if cleaner_manas[x][1] == cleaner_manas[x+1][1]:
						mana_number = (str(int(cleaner_manas[x][0]) + int(cleaner_manas[x+1][0])))
						del cleaner_manas[x+1]
						cleaner_manas[x] = mana_number + cleaner_manas[x][1]
			except IndexError:
				pass
		manaValue = ""
		for item in cleaner_manas:
			manaValue = manaValue + item + " "
		manaValue = manaValue[:len(manaValue)-1]
		return(manaValue)
	except KeyError:
		return "0"

<<<<<<< HEAD
<<<<<<< HEAD
if sys == "Linux":
	directory = "sets/JSON-SetFiles/"
elif sys == "Windows":
	directory = ("JSON-SetFiles")
os.chdir(directory)				#This line adapts to repertoire.py's place which would be in ../ from this file
files = glob.glob("*.json")
#print(files)					#In case of debugging, this line will print all the sets in the order where this program goes through them 09082019@0136Z Esteban Carrillo
SetFileCreator(sys)
=======
=======
>>>>>>> origin/devel
os.chdir("sets/JSON-SetFiles/")				#This line adapts to repertoire.py's place which should be in ../ from this file
files = glob.glob("*.json")
#print(files)					#In case of debugging, this line will print all the sets in the order where this program goes through them 09082019@0136Z Esteban Carrillo
SetFileCreator(files)
<<<<<<< HEAD
>>>>>>> origin/devel
=======
>>>>>>> origin/devel
for mtgSet in files:
	if sys == "Linux":
		mtgSetFile = ("../TXT-SetFiles/"+mtgSet[:-5]+".txt")
	elif sys == "Windows":
		mtgSetFile = ("../TXT-SetFiles/"+mtgSet[:-5]+".txt")
	with open(mtgSetFile,"w+", encoding='UTF-8' ) as SetFile:
		with open(mtgSet, encoding='UTF-8' ) as f:
		    data = json.load(f)

		card_list = []
		for cards in data["cards"]:
			card = []
			try:
				card.append(int(cards["number"]))
			except ValueError:
				card.append(cards["number"])
			card.append(rarity(cards))
			card.append(cards["name"])
			card.append(manaCost(cards))
			card.append(cards["type"])
			try:
				card.append((cards["power"] + "/" + cards["toughness"]))
			except KeyError:
				pass
			card_list.append(card)
			if type(card[0]) != int:
				card_list.remove(card)
		card_list.sort()

		for raw_card in card_list:
			raw_card[0] = str(raw_card[0])
			if len(raw_card[0]) == 1:
				raw_card[0] = "00" + raw_card[0]
			elif len(raw_card[0]) == 2:
				raw_card[0] = "0" + raw_card[0]
			formatted_card = raw_card
			card = ""
			for element in formatted_card:
				card = card + str(element) + '"'
			card = card[:len(card)-1]
			SetFile.write(card + "\n")
	SetFile.close()

print("setparser.py is done")
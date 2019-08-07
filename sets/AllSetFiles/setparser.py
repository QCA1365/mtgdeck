import json


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
		return(cleaner_manas)
	except KeyError:
		return "0"

card_list = []
card_set = input("Quel set? ").upper() + ".json"
with open(card_set) as f:
    data = json.load(f)

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
	try:
		if cards["isOnlineOnly"] == True:
			card_list.remove(card)
	except KeyError:
		pass
card_list.sort()

for raw_card in card_list:
	raw_card[0] = str(raw_card[0])
	if len(raw_card[0]) == 1:
		raw_card[0] = "00" + raw_card[0]
	elif len(raw_card[0]) == 2:
		raw_card[0] = "0" + raw_card[0]
	formatted_card = raw_card
	print(formatted_card)
# Beginning of imports

import os
import glob
import json

# End of imports

os.chdir("/usr/share/powder/mtgdeck/sets/AllSetFiles")
files = glob.glob("*.json")
for mtgSet in files:
	with open(mtgSet) as f:
	    data = json.load(f)
	card_list = []
	for cards in data["cards"]:
		card = []
		try:
			card.append(int(cards["number"]))
		except ValueError:
			card.append(cards["number"])
		card.append(cards["rarity"])
		card.append(cards["name"])
		try:
			card.append(cards["manaCost"])
		except KeyError:
			card.append("0")
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
		except ValueError:
			pass
	try:
		card_list.sort()
	except:
		TypeError

	for raw_card in card_list:
		raw_card[0] = str(raw_card[0])
		if len(raw_card[0]) == 1:
			raw_card[0] = "00" + raw_card[0]
		elif len(raw_card[0]) == 2:
			raw_card[0] = "0" + raw_card[0]
		preformatted_card = raw_card
		formatted_card = ""
		for item in preformatted_card:
			formatted_card = formatted_card + item + ","
		formatted_card = formatted_card[:len(formatted_card)-1]
		print(formatted_card + " ---> " + mtgSet)
import json
import os

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
	card.append(cards["rarity"])
	card.append(cards["name"])
	try:
		card.append(cards["manaCost"])
	except KeyError:
		pass
	card.append(cards["type"])
	try:
		card.append((cards["power"] + "/" + cards["toughness"]))
	except KeyError:
		pass
	card_list.append(card)
	if type(card[0]) != int:
		card_list.remove(card)
	if cards["isOnlineOnly"] == True:
		card_list.remove(card)
card_list.sort()
#print(card_list)
for x in card_list:
	print(x)
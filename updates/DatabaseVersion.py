import json
import os
import platform
import requests

sys = platform.system()

try:
	r = requests.get('https://www.mtgjson.com/json/version.json')
	info = r.json()
	DataVersion = info["version"]

	with open(("updates/version.txt"), "r") as VersionFile:
		version = VersionFile.readlines()
	VersionFile.close()

	if version[0] == DataVersion:
		pass

	else:
		exec(open('sets/setparser.py').read())
		exec(open("inventory/maker.py").read())

		VersionFile = open("updates/version.txt","w+")
		VersionFile.write(DataVersion)
		VersionFile.close()
			
except:
	print('You are not connected to Internet, mtgdeck will NOT update')
	pass
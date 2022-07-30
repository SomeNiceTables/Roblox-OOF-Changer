# Roblox Oof Changer wowowowoow
# Made By SomeNiceTables#9850
# you must have the latest version of roblox for it to work

import urllib.request, json, requests, getpass, shutil
print("Checking Roblox version")

with urllib.request.urlopen("https://api.whatexploitsare.online/logs/Comet/1") as url:
    data = json.loads(url.read().decode())

for i in range(len(data)):
    dictionary = data[i]

cometstuff = dictionary['1']

print("Downloading normal oof file")

request = requests.get("https://cdn.discordapp.com/attachments/985478681793282128/1001625277740351488/uuhhh-1.ogg")
open("ouch.ogg", "wb").write(request.content)
user = getpass.getuser()

destination1 = r"C:\Users\\"
destination2 = "\AppData\Local\Roblox\Versions\\"

print("Replace new OOF File with old one")

shutil.move("ouch.ogg", destination1 + user + destination2 + cometstuff["roblox_version"] + "\content\sounds\ouch.ogg")
input("Done (press enter to exit)")
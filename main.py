# Roblox Oof Changer wowowowoow
# Made By SomeNiceTables#9850
# you must have the latest version of roblox for it to work
# also make sure the script is up to date if it doesnt work, if it doesnt work contact me
# Some error messages are listed in the readme file and solutions to solve it

import urllib.request, json, requests, getpass, shutil
print("Checking Roblox version")

with urllib.request.urlopen("https://api.whatexploitsare.online/status") as url:
    data = json.loads(url.read().decode())

for i in range(len(data)):
    dictionary = data[i]

cometstuff = dictionary["ROBLOX"]

print("Downloading normal OOF file")

request = requests.get("https://raw.githubusercontent.com/SomeNiceTables/Roblox-OOF-Changer/main/oof.ogg")
open("ouch.ogg", "wb").write(request.content)
user = getpass.getuser()

destination1 = r"C:\Users\\"
destination2 = "\AppData\Local\Roblox\Versions\\"

print("Replacing new OOF File with old one")

shutil.move("ouch.ogg", destination1 + user + destination2 + cometstuff["version"] + "\content\sounds\ouch.ogg")
input("Done (press enter to exit)")



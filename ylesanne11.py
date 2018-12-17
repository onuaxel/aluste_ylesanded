#TODO
#Kasutaja sisestab oma lemmiklooma, väljasta väljasta selle muutuja esimene täht
#Koosta list, mis koosneb kolmest loomast, lisa selle listi lõppu kasutaja lemmikloom, 
# väljasta list, väljasta listi viimase elemendi viimane täht
#(sõne kui list, mitmemõõtmeline list - multi dimensional)

userPet=input("Mis on su lemmik loom? ").capitalize()
print(userPet[0])
threeAnimals=["Lõvi", "Kõrberebane", userPet]
print(f"Järjendi 'threeAnimals' sisu: {threeAnimals}")
print(f"Järjendi viimase elemendi viimne täht on: {threeAnimals[-1][-1]}")
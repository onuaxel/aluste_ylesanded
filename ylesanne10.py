#TODO
#Anna muutuja väärtuseks list kolmest oma lemmik puuviljast ja väljasta see
#Väljasta listi esimene väärtus
#Lisa listi lõppu uus puuvili
#Väljasta listi viimane väärtus
#Muuda ühe elemendi väärtust ja väljasta kogu list
#Kontrolli kas väärtus (näiteks õun) eksisteerib listis
#Väljasta listi pikkus
#Eemalda listist element ja väljasta kogu list
#Muuda listi järjekord vastupidiseks
#Sorteeri list ja väljasta
#(jada, list, listi element, listi funktsioonid)

threeFavFruits=["apple", "pear", "cherry"]
print(threeFavFruits)
print(f"Esimene puuvili: {threeFavFruits[0]}")
threeFavFruits[1]="plum"
print(threeFavFruits)
if "apple"  in threeFavFruits:
    print("Alles gut")
print(f"Järjendi pikkus on {len(threeFavFruits)} elementi")
threeFavFruits.pop(-1)
print(threeFavFruits)
reversedThreeFavFruits=threeFavFruits[::-1]
print(f"pööratud järjend: {reversedThreeFavFruits}")
print(f"pööratud ja sorteeritud järjend: {sorted(reversedThreeFavFruits)}")
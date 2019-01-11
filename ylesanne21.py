#TODO
#Koosta dictionary vähemalt viie endale iseloomuliku tunnusega (näiteks: eesnimi, perenimi, sünniaasta, elukoht, lemmik magustoit).
#Väljasta elukoht kahel erineval viisil (kasutades get() meetodit ja mitte kasutades seda).
#Muuda magustoidu väärtust.
#Tee kordus üle dictionary ja väljasta kõik võtmed.
#Tee kordus üle dictionary ja väljasta kõik väärtused (pööra tähelepanu sellele, et saab mitmel viisil, proovi erinevaid võimalusi).
#Kontrolli, kas isikukood on dictionary's olemas.
#Leia dictionary suurus (elementide arv).
#Lisa element pikkus.
#Eemalda element sünniaasta (pane tähele, et saab mitut moodi).
#Pane tähele, et del võtmesõnaga on võimalik kogu dictionary kustutada.
#Saa aru ja katseta del võtmesõna ja clear meetodi erinevusest.
#Tutvu kõigi dictionary meetoditega.
#Läbi ülesanne juhendi lõpus.

#https://www.w3schools.com/python/python_dictionaries.asp

personalData={
    "firstname":"Peeter", 
    "surname":"Putitaja", 
    "birthYear":1999, 
    "placeOfResidence":"Eesti Vabariik", 
    "favDessert":"suhkruvatt"
    }
print(personalData["placeOfResidence"])

print(personalData.get("placeOfResidence"))

personalData["favDessert"]="maasikavaht"

for key in personalData:
    print(key)

print("_"*50)
for key, value in personalData.items():
    print(f"{key}:  {value}")

print("_"*50)
for key, value in personalData.items():
    print(f"{value}")

print("_"*50)
for key in personalData:
    print(personalData[key])

print("_"*50)
if "nationalIdentificationNo" in personalData:
    print("Isikukood olemas")
else:
    print("Isikukood puudu")

print(f"Sõnastiku pikkus on {len(personalData)} kirjet")

personalData["stature"] = 1.99

personalData.pop("birthYear")

personalData.clear()
print(personalData)

del personalData
try:
    print(personalData) 
except NameError:
    print("Sõnastik on kustutatud")

    
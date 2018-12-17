#TODO
#Kirjuta programm, mis küsib kasutajalt nime, 
# tervitab teda nimepidi, küsib kasutajalt elukoha, 
# kui elukoht on Saaremaa, siis väljastab mingi kommentaari, 
# küsib kasutajalt vanuse, kui vanus on väiksem kui 18, 
# siis ütleb, et kasutaja on liiga noor, et autot juhtida, kui vanus on 18, 
# siis õnnitleb täisealiseks saamise puhul, kui kasutaja on vanem kui 18, 
# siis ütleb, et kasutaja võib autot juhtida. (sõne - string)

usersName=input("Mis su nimi on? ").capitalize()
print(f"Tere, {usersName}!")
placeOfResidence=input("Mis maakonnas sa elad? ")
if  "saaremaa" in placeOfResidence.casefold():
    print("Normaalne!")
usersAge=int(input("Kui suur on su vanus? "))
MAGICNUMBER=18
if usersAge == MAGICNUMBER:
    print("Palju õnne täisealiseks saamise puhul!")
elif usersAge<MAGICNUMBER:
    print("Oled liiga noor, et autot juhtida")
elif usersAge>MAGICNUMBER:
    print("Võid autot juhtida")
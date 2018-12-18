#TODO
#Leia muutuja abil etteantud tekstis olevate täishäälikute (a, e, i, o, u, õ, ä, ö, ü) arv. 

someText="Leia muutuja abil etteantud tekstis olevate täishäälikute (a, e, i, o, u, õ, ä, ö, ü) arv."
vowelCounter=0
vowels=["a","e","i","o","u","õ","ä","ö","ü"]

for character in someText.lower():
    if character in vowels:
        vowelCounter+=1
        
print(vowelCounter)

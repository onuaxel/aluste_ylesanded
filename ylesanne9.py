#TODO
#Kolmnurki liigitatakse külgede pikkuse järgi erikülgseteks, 
# võrdhaarseteks ja võrdkülgseteks. Kirjutada programm, 
# mis küsib kasutajalt kolme külje pikkused ning 
# väljastab vastusena kolmnurga liigi. 
# Lisaks tuleb kontrollida, kas etteantud küljepikkustega 
# kolmnurk saab üldse eksisteerida. 
# Külje pikkused ei pea olema täisarvud. (ujukomaarv - float)
triangleSides=set()
for triangleSide in range(1,4):
    side=float(input(f"Sisesta kolmnurga {triangleSide}. külje pikkus: "))
    triangleSides.add(side)

def isTriangle(triangleSides):
    longestSide=max(triangleSides)
    shortestSide=min(triangleSides)
    triangleSides.remove(longestSide)
    shorterSide=max(triangleSides)
    if longestSide<(shorterSide+shortestSide):
        return True
    else:
        return False

if len(triangleSides)==1:
    print("Tegu on võrdkülgse kolmnurgaga")
elif len(triangleSides)==2:
    if isTriangle(triangleSides):
        print("Tegu on võrdhaarse kolmnurgaga")
    else:
        print("Säherduste mõõtmete korral ei saa kolmnurk eksisteerida")
elif len(triangleSides)==3:
    if isTriangle(triangleSides):
        print("Tegu on erikülgse kolmnurgaga")
    else:
        print("Säherduste mõõtmete korral ei saa kolmnurk eksisteerida")
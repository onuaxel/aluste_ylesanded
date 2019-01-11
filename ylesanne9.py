#TODO
#Kolmnurki liigitatakse külgede pikkuse järgi erikülgseteks, 
# võrdhaarseteks ja võrdkülgseteks. Kirjutada programm, 
# mis küsib kasutajalt kolme külje pikkused ning 
# väljastab vastusena kolmnurga liigi. 
# Lisaks tuleb kontrollida, kas etteantud küljepikkustega 
# kolmnurk saab üldse eksisteerida. 
# Külje pikkused ei pea olema täisarvud. (ujukomaarv - float)

triangleEdges=[]
for triangleSide in range(1,4):
    side=float(input(f"Sisesta kolmnurga {triangleSide}. külje pikkus: "))
    triangleEdges.append(side)

def isTriangle(edge):
    longestSide=max(edge)
    shortestSide=min(edge)
    edge.remove(longestSide)
    edge.remove(shortestSide)
    shorterSide=edge[0]
    if longestSide<(shorterSide+shortestSide):
        return True
    else:
        return False

triangleSides=set(triangleEdges)

if len(triangleSides)==1:
    print("Tegu on võrdkülgse kolmnurgaga")
elif len(triangleSides)==2:
    if isTriangle(triangleEdges):
        print("Tegu on võrdhaarse kolmnurgaga")
    else:
        print("Säherduste mõõtmete korral ei saa kolmnurk eksisteerida")
elif len(triangleSides)==3:
    if isTriangle(triangleEdges):
        print("Tegu on erikülgse kolmnurgaga")
    else:
        print("Säherduste mõõtmete korral ei saa kolmnurk eksisteerida")
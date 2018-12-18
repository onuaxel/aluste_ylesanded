#TODO
#Kirjutada programm, mis kontrollib, 
# kas antud positiivne täisarv on liig- või lihtaasta number. 
# (Aasta on liigaasta, kui tema number jagub neljaga, 
# välja arvatud need aastad, mille number jagub sajaga, kuid ei jagu neljasajaga.)
#VIGANE SELGITUS, PEAKS OLEMA Iga aasta, mis jagub neljaga, on liigaasta (kui ta samal ajal ei jagu sajaga). Kui aasta jagub sajaga, siis ta ei ole liigaasta. Aasta, mis jagub neljasajaga, on igal juhul liigaasta. (https://et.wikipedia.org/wiki/Liigaasta)


year=int(input("Anna siva üks aasta number "))
if (year%4==0 and year%100!=0) or year%400==0:
    print("liig")

else:
    print("liht")
#TODO
#Kirjutada programm, mis kontrollib, 
# kas antud positiivne täisarv on liig- või lihtaasta number. 
# (Aasta on liigaasta, kui tema number jagub neljaga, 
# välja arvatud need aastad, mille number jagub sajaga, kuid ei jagu neljasajaga.)

year=int(input("Anna siva üks aasta number "))
if (year%4==0 and year%100==0 and year%400!=0):
    print("liig")
else:
    print("liht")

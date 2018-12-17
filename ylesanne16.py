#TODO
#Arvu arvamise mäng. 
#Arvuti mõtleb välja arvu nullist sajani. 
# Lase kasutajal pakkuda, mis arvu arvuti välja mõtles. 
# Vale pakkumise korral annab arvuti vihje, kas pakkumine on õigest arvust suurem 
# või väiksem. Pakkuda saab seni, kuni kasutaja on õige arvu pakkunud. 
# (juhuarv - random)
from random import random

computersRandomNumber = int(random()*100)

usersInput=input("Mis arvu arvuti sinu arvates genereeris: ")
try:
    usersGuess=int(usersInput)
    while usersGuess!=computersRandomNumber:
        if usersGuess<computersRandomNumber:
            print("Raali arv on suurem.")
            usersGuess=int(input("Paku uuesti: "))
        elif usersGuess>computersRandomNumber:
            print("Raali arv on väiksem.")
            usersGuess=int(input("Paku uuesti: "))
    print("Juhuu! Õige vastus!")
except ValueError:
    print("ERROR: F057XE241")
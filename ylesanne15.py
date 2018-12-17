#TODO
#Väljasta korduslause abil 8 korrutis arvudega 0..12
#8 x 0 = 0
#	8 x 1 = 8
#	8 x 2 = 16
#	…
#	8 x 12 = 96
#Täienda programmi nii, et kasutajalt küsitakse arv x, mille kohta korrutustabel väljastatakse
CONSTANT=8
def multiplication_table(multiplicand):
    multiplicator=0
    while multiplicator <=12:
        answer=multiplicand*multiplicator
        print(f"{multiplicand} x {multiplicator} = {answer} ")
        multiplicator+=1
multiplication_table(8)


userWish=int(input("Palun sisesta täisarv, mille kohta korrutustabelit soovid: "))
multiplication_table(userWish)
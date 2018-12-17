#TODO
#Kivi-paber-käärid mäng. 
#Arvuti mõtleb välja ühe variandi - kivi, paber või käärid. Arvuti küsib kasutaja valikut. 
# Programm ütleb, kes võitis.
#Täienda programmi nii, et mängitakse seni, kuni kasutaja ei taha enam mängida.

from random import randint

#Define function to gen "paper","scissors" or "rock"
def computersChoice():
    computersGuess=randint(0,2)
    if computersGuess==0:
        return "kivi"
    elif computersGuess ==1:
        return "paber"
    else:
        return "käärid"

#Define function to ask users choice and save it
def humansChoice():
    humansChoice=input("Kivi (1), paber (2) või käärid (3)? ").lower()
    if humansChoice == "1" or humansChoice=="kivi":
        answer = "kivi"
    elif humansChoice =="2" or humansChoice == "paber":
        answer = "paber"
    elif humansChoice =="3" or humansChoice == "käärid":
        answer = "käärid"
    else:
        answer="Arusaamatu vastus"
    return answer
    
playerOne="arvuti!"
palyerTwo="inimene!"
rockWinsScissors="Kivi nüristab käärid. Võitis "
paperWinsRock="Paber katab kivi. Võitis "
scissorsWinsPaper="Käärid lõikavad paberi katki. Võitis "
tie="Viik, keegi ei võitnud"
gameIsOn=True

#Define function to find out who has won
def compareAnswers(computersAnswer, humansAnswer):
    result=""
    if computersAnswer==humansAnswer:
        result=tie

    elif computersAnswer == "kivi" :
        if humansAnswer == "käärid":
            result=rockWinsScissors+playerOne
        elif humansAnswer == "paber":
            result=paperWinsRock+palyerTwo

    elif computersAnswer == "paber":
        if humansAnswer == "käärid":
            result=scissorsWinsPaper+palyerTwo
        elif humansAnswer == "kivi":
            result=paperWinsRock+playerOne

    elif computersAnswer =="käärid":
        if humansAnswer == "paber":
            result=scissorsWinsPaper+playerOne
        elif humansAnswer == "kivi":
            result=rockWinsScissors+palyerTwo

    print(result)

while gameIsOn:
    computersAnswer=computersChoice()
    humansAnswer=humansChoice()
    print(f"Arvuti: {computersAnswer}")
    print(f"Inimene: {humansAnswer}")
    compareAnswers(computersAnswer, humansAnswer)
    shallWePlayAgain=input("Teeme uuesti (1)? Või pigem mitte (0)? ").lower()
    print("-"*35)
    if (shallWePlayAgain=="jah" or shallWePlayAgain=="ok" )or shallWePlayAgain=="1":
        gameIsOn=True
    else:
        gameIsOn=False
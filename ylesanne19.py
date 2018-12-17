#TODO
#Kaardimäng Blackjack
#https://et.wikipedia.org/wiki/Blackjack

import random
from random import randint

def createCardRanks(suit):
    for number in range(2,11):
            card=(suit, number)
            cardDeck.append(card)
    jack=(suit, "Jack")
    cardDeck.append(jack)
    queen=(suit, "Queen")
    cardDeck.append(queen)
    king=(suit, "King")
    cardDeck.append(king)
    ace=(suit, "Ace")
    cardDeck.append(ace)

#Create card deck
cardDeck=[]
for suit in range(1,5):
    if suit==1:
        suit="Club"
        createCardRanks(suit)
    elif suit ==2:
        suit="Spade"
        createCardRanks(suit)
    elif suit ==3:
        suit="Diamond"
        createCardRanks(suit)
    elif suit ==4:
        suit="Heart"
        createCardRanks(suit)

#Shuffle the card deck
random.shuffle(cardDeck)
dealersHand=[]
playersHand=[]

#Define function to deal a card from deck to hand and show the hand
def dealACard(hand):
    hand.append(cardDeck[0])
    del cardDeck[0]
    showHand(hand)

def countScore(hand):
    score=0
    #Sum the card values to a score
    for card in range(0,len(hand)):
        if (hand[card][-1]) == "Jack" or (hand[card][-1]) == "Queen" or (hand[card][-1]) == "King":
            score+=10

        elif (hand[card][-1]) in range(2,11):
            score+=(hand[card][-1])

    #check if the hand includes ace card
    for card in range (0,len(hand)):
        if   (hand[card][-1]) == "Ace":
            if score>(21-11):
                score+=1
            elif score<=(21-11):
                score+=11
    return score

#Define function to ask if player wants one more card
def playerWantsMore():
    palyersChoice=input("Hit(1) or stand(2)? ").lower()
    if palyersChoice == "1" or palyersChoice=="hit":
        return 1
    elif palyersChoice =="2" or palyersChoice == "stand":
        return 2
    else:
        print("Answer not accepted!")
        playerWantsMore()

#Define function which shows cards in hand
def showHand(hand):
    if hand == dealersHand:
        firstCardFaceDown=[]
        firstCardFaceDown.extend(dealersHand)
        firstCardFaceDown[0]=('x','x')
        print(f"Dealers hand: {firstCardFaceDown}")
    else:
        print(f"Players hand: {playersHand}")


print("ↀ"*50)
print("\nDealing first card: ")
dealACard(playersHand)
dealACard(dealersHand)
print("-"*50)

print("Dealing second card: ")
dealACard(playersHand)
dealACard(dealersHand)
print("\nↀ"+"ↀ"*49)

while True:
    playersWish=playerWantsMore()
    if countScore(playersHand)>21:
        print(f"Score: {countScore(playersHand)}. Player has gone bust!")
        print("Game over, loser!")
        break

    elif playersWish==2:
        print(f"Dealer reveals it's whole hand: {dealersHand}")
        dealersScore=countScore(dealersHand)
        playersScore=countScore(playersHand)
        print(f"Players end score: {playersScore}")
        print(f"Dealers end score: {dealersScore}")
        if dealersScore>21:
            if playersScore>21:
                print("No one wins!")
                break
            elif playersScore<=21:
                print("Player wins!")
                break
        elif dealersScore<21:
            if playersScore>21:
                print("Dealer wins!")
                break
            elif playersScore<21:
                if dealersScore>playersScore:
                    print("Dealer wins!")
                    break
                else:
                    print("Player wins!")
                    break
            break
    
    elif playersWish==1:
        print("\nDealing extra card: ")
        dealACard(playersHand)
        if countScore(playersHand)>21:
            print(f"Score: {countScore(playersHand)}. Player has gone bust!")
            print("Game over, loser!")
            break
        dealACard(dealersHand)
        print("-"*50)
    
    
print("ↀ"*50)
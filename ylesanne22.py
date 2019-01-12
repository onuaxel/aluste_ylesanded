#TODO
#
#https://www.reddit.com/r/dailyprogrammer/comments/8xzwl6/20180711_challenge_365_intermediate_sales/
#
#Lisatasu arvutamise ülesanne. Alusta algoritmi koostamisest. Kommentaarides on kah lahendused, aga proovi ise lahendada. Defineeri lisatasu arvutamise funktsioon. Sisendina defineeri dictionary.
revenue={"Frank":{"Tea":120, "Coffee":243}, "Jane":{"Tea":145, "Coffee":265}}
expenses={"Frank":{"Tea":130, "Coffee":143}, "Jane":{"Tea":59, "Coffee":198}}

#Sales people get paid using the following formula for the total commission: commission is 6.2% of profit, with no commission for any product to total less than zero.
def profit(revenue, expenses):
    profit={}
    people=[]
    drinks=[]
    for key in revenue:
        people.append(key)
    for key in revenue[people[0]]:
        drinks.append(key)
    #profit=revenue-expense
    for worker in range(len(people)):
        personalRevenue=revenue[people[worker]]
        personalExpens=expenses[people[worker]]
        print(people[worker])
        # print(personalRevenue)
        # print(personalExpens)

        for drink in range(len(drinks)):
            print(drinks[drink])
            print(personalRevenue[drinks[drink]]-personalExpens[drinks[drink]])
profit(revenue, expenses)
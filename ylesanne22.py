#TODO
#
#https://www.reddit.com/r/dailyprogrammer/comments/8xzwl6/20180711_challenge_365_intermediate_sales/
#
#Lisatasu arvutamise ülesanne. Alusta algoritmi koostamisest. Kommentaarides on kah lahendused, aga proovi ise lahendada. Defineeri lisatasu arvutamise funktsioon. Sisendina defineeri dictionary.
revenue={"Frank":{"Tea":120, "Coffee":243}, "Jane":{"Tea":145, "Coffee":265}}
expenses={"Frank":{"Tea":130, "Coffee":143}, "Jane":{"Tea":59, "Coffee":198}}

#Sales people get paid using the following formula for the total commission: commission is 6.2% of profit, with no commission for any product to total less than zero.
def profit(revenue, expenses):
    commissions={}
    people=[]
    drinks=[]
    for key in revenue:
        people.append(key)
    for key in revenue[people[0]]:
        drinks.append(key)
    
    for worker in range(len(people)):
        profits=[]
        personalRevenue=revenue[people[worker]]
        personalExpens=expenses[people[worker]]
        for drink in range(len(drinks)):
            profit=personalRevenue[drinks[drink]]-personalExpens[drinks[drink]]
            if profit<0:
                profit=0
            profits.append(profit)
        commision=sum(profits)*0.062
        commissions[people[worker]]=round(commision, 2)
    return commissions
    
print(profit(revenue, expenses))
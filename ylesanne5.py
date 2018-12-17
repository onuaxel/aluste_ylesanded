user_input=input("Palun sisesta summa kroonides: ")
excangeRate=15.6466
eek=0
if "." in user_input:
    try:
        eek =  float(user_input)
    except ValueError:
        print("Kas sa ikka sisestasid summa numbritega?")
elif "," in user_input:
    try:
        commaReplaced = user_input.replace("," , ".")
        eek =  float(commaReplaced)
    except ValueError:
        print("Kas sa ikka sisestasid summa numbritega?")
else :
    try :
        eek = int(user_input)
    except ValueError:
        print("Kas sa ikka sisestasid summa numbritega?")
        
moneyInEur = round((eek*excangeRate),2)
print(f"See kogus raha on eurodes {moneyInEur}€" )
#https://www.reddit.com/r/dailyprogrammer/comments/a72sdj/20181217_challenge_370_easy_upc_check_digits/
#
#UPC vöötkoodi kontrollsumma arvutamise ülesanne. Alusta algoritmi koostamisest. Kommentaarides on kah lahendused, aga proovi ise lahendada. Defineeri kontrollsumma arvutamise funktsioon. (https://www.w3schools.com/python/python_functions.asp)

UPC="12345678910"
def checkSumCalc(UPC):
    startingUPC=UPC
    oddSum=[]
    evenSum=[]
    standardLength=12
    if  len(UPC)<standardLength-1:
        UPC=UPC.zfill(standardLength-1)
    for i in range(0,len(UPC),2): #gen "odd" numbers for 0-based indexing
        oddSum.append(int(UPC[i])) 
    rule1=sum(oddSum)#rule no1: sum of all odd-numbered positions
    rule2=rule1*3 #rule no2: multiply the result from step 1 by 3
    for i in range(1,len(UPC),2): #gen "even" numbers for 0-based indexing
        evenSum.append(int(UPC[i]))
    rule3=sum(evenSum)+rule2 #rule no3 Take the sum of digits at even-numbered positions (2nd, 4th, 6th, ..., 10th) in the original number, and add this sum to the result from rule no2
    rule4=rule3%10
    if rule4 ==0 :
        checkSum=0
    else:
        checkSum=10-rule4
    print(f"upc({startingUPC}) => {checkSum}")

checkSumCalc(UPC)
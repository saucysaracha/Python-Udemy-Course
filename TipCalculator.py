#Day 2 : Tip Calculator

totalBill = float(input("What was the total bill? $"))
percentageTip = float(input("What percentage tip would you like to give? 10, 12, or 15? "))
numberOfPeople = int(input("How many people to split the bill? "))

percentageTip /= 100
newTotalBill = totalBill + (totalBill * percentageTip)
#print(type(newTotalBill))
billPerPerson = round((newTotalBill / numberOfPeople), 2)
#round(billPerPerson, 2)
print(f"Each person should pay: ${billPerPerson}")
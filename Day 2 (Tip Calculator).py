print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10%, 12%, or 15% "))
people = int(input("How many people to split the bill? "))

tipPercentage = tip / 100
tipTotal = bill * tipPercentage
billTotal = bill + tipTotal
billPerPerson = billTotal / people
finalAmount = round(billPerPerson, 2)

print(f"Each person should pay: ${finalAmount}")

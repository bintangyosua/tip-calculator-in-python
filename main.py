# Days 2 - Final Project
print("Welcome to the tip calculator")
totalBill = float(input("What was the total bill? $"))
percentage = float(input("What percentage tip would you like to give? 10, 12, or 15? "))
totalPerson = float(input("How many people to split the bill? "))

bill = totalBill/totalPerson*(1 + (percentage/100))
print(f"Each person should pay: {round(bill, 2)}")
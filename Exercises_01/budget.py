# This Python script is written by Vinay Reddy B

print("Prepared by Vinay Reddy B")

#considering this semester as 3 months
Budget = int(input("Enter the Budget amount for this semester"))
Houserent = int(input("Enter the house rent per month"))
Groceries = int(input("Enter the approx groceries bill per month"))
ELectricitybill = int(input("Enter the approx Electricity bill per month"))
Personalexpences = int(input("Enter the approx Personal Expences per month"))
Total = (Houserent+Groceries+ELectricitybill+Personalexpences)*3
final = Budget-Total
if Budget>Total:
    print("You are left with Euros", final)
elif Total>Budget:
    print("Your total expeditures are exceeding your budget, plan accourdingly with your budget amount of Euros", final)
elif Total==Budget:
    print("Your Budget and expenditure are equal.")
else:
    print("Please provide proper inputs in the form of integers")
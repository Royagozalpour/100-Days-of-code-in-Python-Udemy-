print("Welcome to the tip calculator")
Totalbill = (float(input("What was the total bill? ")))
Tip = (int(input("How much tip would you like to give? 10, 12 or 15? ")))
Split = (int(input("How many people to split the bill? ")))
tot = float((Totalbill // Split) + (Tip/100))
print(f"each person should pay:{tot}")
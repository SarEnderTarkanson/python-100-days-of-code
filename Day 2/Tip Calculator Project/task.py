print("Welcome to the tip calculator!\n")
bill = float(input("What was the total bill? $\n"))
tip = int(input("What percentage tip would you like to give? 10 12 15 \n"))
people = int(input("How many people to split the bill? \n"))
tip = bill * (tip/100)
total = round((bill + tip), 2)
result = total / people
result = round(result, 2)
print(f"Each person should pay\n{result}")



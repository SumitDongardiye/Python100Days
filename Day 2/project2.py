print("Welcome to the tip calculator!\n")
total=int(input("What was the total bill? $"))
tip= int(input("How much tip would you like to give? 10, 12, or 15? "))
people= int(input("Ho many people to split the bill?"))
result= (total + (tip/100*total))/people
print(f"Each person should pay: ${result}")
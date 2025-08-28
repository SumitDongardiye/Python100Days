height=int(input("Enter your height? "))
if height>=120:
    print("You can ride")
    age=int(input("Enter your age? "))
    if age<12:
        print("You need to pay $5")
    elif age>=12 and age<=18:
        print("You need to pay $7")
    else:
        print("You need to pay $12")
else:
    print("Can't ride")
height=int(input("Enter your height? "))
bill=0

if height>=120:
    print("You can ride")
    age=int(input("Enter your age? "))
    if age<12:
        print("Child tickets are $5")
        bill=5
    elif age>=12 and age<=18:
        print("Youth tickets are $7")
        bill=7
    else:
        print("Adult ticekts are $12")
        bill=12
    photo=input("Do you want to have a photo take? Type y for Yes and n for No.")

    if photo =='y':
        bill+=3

    print(f"Your final bill is ${bill}")

else:
    print("Can't ride")
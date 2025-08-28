import random

user_input=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))
computer_input=random.randint(0,2)
print(f"Computer Chooose {computer_input}")

if user_input==0 and computer_input==0:
    print("Draw")
elif user_input==0 and computer_input==1:
    print("Computer Wins")
elif user_input==0 and computer_input==2:
    print("You Win!")
elif user_input==1 and computer_input==0:
    print("You Win!")
elif user_input==1 and computer_input==1:
    print("Draw")
elif user_input==1 and computer_input==2:
    print("Computer Wins")
elif user_input==2 and computer_input==0:
    print("Computer Wins")
elif user_input==2 and computer_input==1:
    print("you Win!")
elif user_input==2 and computer_input==2:
    print("Draw")
else:
    print("Invalid Input")
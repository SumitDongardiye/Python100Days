import random
def guess(number,attempt):
    game=True

    while attempt>0 and game is True:
        attempt-=1
        guess=int(input("Make a guess: "))

        if attempt==0:
            print("You've run out of guesses. Refresh the page to run again")
        elif guess==number:
            print(f"You guessed the number {number} correct!")
            game=False
        elif number<guess:
            print("Too high.")
            print("Guess again")
            print(f"You have {attempt} attempts remaning to guess the number.")
        elif number>guess:
            print("Too low.")
            print("Guess again")
            print(f"You have {attempt} attempts remaning to guess the number.")
        
        


random_number= random.randrange(1,100)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
print(random_number)
difficult=input("Choose a difficulty. Type 'easy' or 'hard': ")

if difficult=="easy":
    print("You have 10 attempts remaining to guess the number")
    guess(random_number,10)
elif difficult=="hard":
    print("You have 5 attempts remaining to guess the number")
    guess(random_number,5)
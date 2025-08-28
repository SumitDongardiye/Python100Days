import random
word_list = ["aardvark","baboon","camel"]

placeholder=""

game_over=False
lives=6

word=random.choice(word_list)
for i in word:
    placeholder+='_'

print(word)
print(placeholder)

correct_letters=[]
while not game_over:
    guess=input("Enter a letter: ").lower()

    display=""
    
    for letter in word:
        
        if guess==letter:
            display+=letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display+=letter
        else:
            display+="_"

    print(display)

    if guess not in word:
        lives-=1
        if lives == 0:
            game_over = True
            print("You lose.")


    if "_" not in display:
        print("You Win!")
        game_over=True
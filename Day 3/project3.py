print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
input1=input('You are at a cross road.Where do you want to go? \n Type "left" or "right"\n')
if input1=='left':
    input2=input("You've come to lake.There is an island in the middle of the lake. \n Type \"wait\" to wait for the boat. Type \"swim\" to swim accross.")
    if input2=='wait':
        input3=input("You arrive at an island unharmed.There is a house with 3 doors. \n One red, one yellow and one blue. Which color do you choose?\n")
        if input3=='red':
            print("It's a room full of fire.Game Over")
        elif input3=='blue':
            print("You enter a room of beasts.Game Over")
        elif input3=='yellow':
            print("You found the treasure! You Win!")
        else:
            print("Wrond Choise. Game Over")
    else:
        print("You get attacked by an angry trout.Game Over.")
else:
    print("You fell into a hole. Game Over")
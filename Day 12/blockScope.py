# There is no Block scope in python!
game_level=6
enemies = ["a","b","c"]

def create_enemy():
    new_enemy=""
    if game_level<5:
        new_enemy= enemies[0]

    print(new_enemy)

# If we create a variable within a function then it's available only within that function
# If we create a variable inside a block then we can use it anywhere in the program file.
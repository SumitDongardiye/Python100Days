enemies=1

def increase_enemies():
    global enemies  # With this we can use the global variable inside a function
    enemies+=1
    print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemis outside function: {enemies}")
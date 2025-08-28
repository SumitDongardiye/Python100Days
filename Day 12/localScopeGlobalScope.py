enemies=1

def increase_enemies():
    enemies=2
    print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemis outside function: {enemies}")


# Local Scope: It's within the function

"""def a():
    b=0   #local scope
    print(b)

a()
print(b)"""

#Global Scope: It's can be accesed anywhere within the program

"""d=1
def c():
    d=2
    print(d)

c()
print(d)"""
import random
friends=["Alice","Bob","Charlie","David","Emanuel"]
# Option 1
length=len(friends)-1
val=random.randint(0,length)
print(friends[val])

# Option 2
print(random.choice(friends))
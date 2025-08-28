# List is a datastructure. It's a way of organizing and storing data in python
# fruits = ["item1", "item2"]
# They have the order and now we can use them in the same order

states_of_india = ["Madhya Pradesh", "Delhi", "Rajasthan","Tamil Nadu"]
print(states_of_india[0],states_of_india[-1])
states_of_india[1]="Maharashtra"   #Update the list
print(states_of_india[1])
states_of_india.append("Uttar Pradesh")  #Used to add item to end of the list
states_of_india.extend(["Chattisgarh","Bihar","Jharkhand"])   #Used to add list at the end of the list

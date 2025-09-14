# new_list= [new_item for item in list]    Syntax
numbers= [1,2,3]
new_list=[n+1 for n in numbers]

print(new_list)

name="Sumit"
new_name=[letter for letter in name]
print(new_name)

demo=range(1,5)
new_demo=[n*2 for n in demo]
print(new_demo)

# Conditional List Comprehension
# new_list=[new_item for item in list if test]
names=["Alex","Beth","Caroline","Dave","Eleanor","Freddie"]
short_name=[a.upper() for a in names if len(a)<5]
print(short_name)
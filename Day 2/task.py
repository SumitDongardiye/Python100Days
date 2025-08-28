#Subscripting
print("Hello"[1])    
print("Hello"[-1])

# String
print("123"+"345")

# Integer = Whole number
print(123 + 345)

# Large Integer
print(123_456_789)

# Float = Floating Point Number
print(314.59)

# Boolean 
print(True)
print(False)

#Type Error
# len(123) it gives error as len functions does not accept integer as argument
print(len(str("123")))

# Check data type using type function
# Type Checking
print(type(123))
print(type("Sumit"))
print(type(False))
print(type(1.24))

#Type Conversion/ Casting
# int, float, str, bool

a=int("123")
print(a+456)

# print("Number of letters in your name: " + str(len(input("Enter your name"))))


# Mathematical Operations in Python
print("My age: " + str(12))
print(123+456)
print(7-3)
print(3*2)
print(5/3)
print(5//3) # if we want the result which has no decimal places, but it only gives the value before decimal point
print(2**2)  # it's used to calculate power of the number

# When there is more than one type of calculation in priority then PEMDAS rule is applied
# ()
# **
# * OR /
# + OR -
# Calculation goes from left to right

print(3*(3+3)/3 -3)

# Number Manipulation & F Strings in Python
bmi = 84 / 1.65 ** 2
print(bmi)
print(int(bmi))

print(round(bmi))
print(round(bmi,2))

# Assignment Operator
# += , -= , *=  , /=

score =0
score +=1
print(score)

# f-string

height =1.0
is_winning= True

print(f"Your score is: {score}, your height is {height}. You are winning is {is_winning}")

# Randomisation: 
# Python uses Mersenne Twister to generate random number
# Random is python module. 
import random
random_int=random.randint(0,10)   #Generates the random number between the range a & b both inclusive
print(random_int)

random_float=random.random()   #Generates random floating number between 0(inclusive) to 1(not inclusive)
print(random_float)

random_float2=random.uniform(1,10)  #Generates random float number between a & b both inclusive
print(random_float2)
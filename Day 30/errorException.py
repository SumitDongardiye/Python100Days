# FileNotFound
# try:
#     file=open("a_file.txt")
#     a_dictionary= {"key":"value"}
#     value=a_dictionary["key"]
#
# except FileNotFoundError:
#     file=open("a_file.txt","w")
#     file.write("Something")
# except KeyError as error_message:
#     print(f"The key {error_message} does no exist.")
# else:
#     content=file.read()
#     print(content)
# finally:
#     raise TypeError("This is an error that I made up")


# KeyError
# a_dictionary= {"key":"value"}
# value=a_dictionary["non_existent_key"]

# IndexError
# fruit_list=["Apple","Banana","Pear"]
# fruit=fruit_list[3]

# TypeError
# text="abc"
# print(text+5)

# try: Something that might cause an exception
# except: Do this if there was an exception
# else: Do this if there were no exception
# finally: Do this no matter what happens
# raise: Used to raise our own exception

# height=float(input("Height: "))
# weight=int(input("Weight: "))
#
# if height>3:
#     raise ValueError("Human Height should not be over 3 meter")
#
# bmi=weight/height**2
# print(bmi)



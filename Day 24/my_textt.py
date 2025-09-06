# with open("my_text.txt") as file:
#     content=file.read()
#     print(content)

with open("new_file.txt",mode="w") as file:
    a=file.write("\n New text2.")
    print(a)

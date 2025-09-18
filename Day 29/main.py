from tkinter import *
from tkinter import messagebox
import random
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_passwordd():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters=[random.choice(letters) for _ in range(nr_letters)]
    password_symbols=[random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers=[random.choice(numbers) for _ in range(nr_numbers)]

    password_list=password_letters+password_symbols+password_numbers
    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0,password)
    pyperclip.copy(password)   #Used to copy text directly into clipboard
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_value():
    website = website_entry.get()
    email= email_entry.get()
    passwords= password_entry.get()

    if len(website)==0 or len(password)==0:
        messagebox.showinfo("Oops", "Please fill all the fields")
    else:

        # Message box
        # messagebox.showinfo(title="Success", message=f"{website} | {email} | {password}")
        is_ok=messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail:{email} \n Password:{password} \nIs it ok to save?")

        if is_ok:
            with open("data.txt","a") as file:
                file.write(f"{website} | {email} | {passwords}\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)
# ---------------------------- UI SETUP ------------------------------- #
window= Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

logo=PhotoImage(file="logo.png")
canvas= Canvas(width=200, height=200)
canvas.create_image(100,100,image=logo)
canvas.grid(column=1, row=0)

# Labels
website_label=Label(text="Website:")
website_label.grid(column=0, row=1)

email_label=Label(text="Email/Username:")
email_label.grid(column=0, row=2)

password_label=Label(text="Password:")
password_label.grid(column=0, row=3)

# Entries
website_entry=Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()  #Focus cursor using this method
email_entry=Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0,"sumd035@gmail.com")
password_entry=Entry(width=18)
password_entry.grid(column=1, row=3)

# Buttons
generate_password=Button(text="Generate Password",command=generate_passwordd)
generate_password.grid(column=2, row=3)

add_button=Button(text="Add", width=36, command=save_value)
add_button.grid(column=1, row=4, columnspan=2)


window.mainloop()
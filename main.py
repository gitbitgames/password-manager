import tkinter as tk
from tkinter import messagebox
from random import randint
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    allowed_chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabdefghijklmnopqrstuvwxyz1234567890~!@#$%^&*()_-+={[}]|\:;<>.?/'
    password = ''.join([allowed_chars[randint(0, len(allowed_chars)-1)] for i in range(14)])
    entry3.delete(0, tk.END)
    entry3.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def add_password():
    website, email, password = entry1.get(), entry2.get(), entry3.get()
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title='Oops', message="Please make sure to fill in all fields.")

    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    is_ok = messagebox.askokcancel(title=website, message=f"These are the details you entered: \nEmail:{email} \nPassword:{password}\nDo you want to save?")

    if is_ok:
        try:
            with open('data.json', 'r') as data_file:
                data = json.load(data_file)

        except FileNotFoundError:
            with open('data.json', 'w') as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)

            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)

        entry1.delete(0, tk.END)
        entry2.delete(0, tk.END)
        entry3.delete(0, tk.END)

def search_password():
    website = entry1.get()
    with open('data.json', 'r') as data_file:
        data = json.load(data_file)
        if website in data:
            entry2.insert(0, data[website]['email'])
            entry3.insert(0, data[website]['password'])


# ---------------------------- UI SETUP ------------------------------- #

window = tk.Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = tk.Canvas(height=200, width=200)
logo_img = tk.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)


label1 = tk.Label(text="Website:")
entry1 = tk.Entry(width=21)
label2 = tk.Label(text="Email/Username:")
entry2 = tk.Entry(width=38)
label3 = tk.Label(text="Password:")
entry3 = tk.Entry(width=21)

search_button = tk.Button(text="Search", width=13, command=search_password)
generate_button = tk.Button(text="Generate Password", command=generate_password)
add_button = tk.Button(text="Add", width=36, command=add_password)

canvas.grid(column=1, row=0)
label1.grid(column=0, row=1)
entry1.grid(column=1, row=1)
label2.grid(column=0, row=2)
entry2.grid(column=1, row=2, columnspan=2)
label3.grid(column=0, row=3)
entry3.grid(column=1, row=3)
search_button.grid(column=2, row=1)
generate_button.grid(column=2, row=3)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
import tkinter as tk
from random import randint

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    allowed_chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabdefghijklmnopqrstuvwxyz1234567890~!@#$%^&*()_-+={[}]|\:;<>.?/'
    password = ''.join([allowed_chars[randint(0, len(allowed_chars)-1)] for i in range(14)])
    entry3.delete(0, tk.END)
    entry3.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def add_password():
    with open('saved.csv', 'a') as f:
        f.write(f'\n{entry1.get()},{entry2.get()},{entry3.get()}')

# ---------------------------- UI SETUP ------------------------------- #

window = tk.Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = tk.Canvas(height=200, width=200)
logo_img = tk.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)


label1 = tk.Label(text="Website:")
entry1 = tk.Entry(width=38)
label2 = tk.Label(text="Email/Username:")
entry2 = tk.Entry(width=38)
label3 = tk.Label(text="Password:")
entry3 = tk.Entry(width=21)

generate_button = tk.Button(text="Generate Password", command=generate_password)
add_button = tk.Button(text="Add", width=36, command=add_password)

canvas.grid(column=1, row=0)
label1.grid(column=0, row=1)
entry1.grid(column=1, row=1, columnspan=2)
label2.grid(column=0, row=2)
entry2.grid(column=1, row=2, columnspan=2)
label3.grid(column=0, row=3)
entry3.grid(column=1, row=3)
generate_button.grid(column=2, row=3)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
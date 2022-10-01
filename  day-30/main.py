import random
import tkinter as tk
from tkinter import messagebox
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    letters_list = [random.choice(letters) for _ in range(nr_letters)]
    symbols_list = [random.choice(numbers) for _ in range(nr_symbols)]
    numbers_list = [random.choice(symbols) for _ in range(nr_numbers)]

    password_list = letters_list + symbols_list + numbers_list
    random.shuffle(password_list)

    password = "".join(password_list)
    pyperclip.copy(password)

    password_input.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    """Gets values {website}, {username}, {password} and appends them in a 'data.txt', then resets all input fields."""

    website = website_input.get()
    username = username_or_email_input.get()
    password = password_input.get()
    new_data = {
        website: {
            'username': username,
            'password': password,
        }
    }

    if len(website) == 0 or len(username) == 0 or len(password) == 0:
        messagebox.showerror(message="Please, leave no empty fields")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
                data.update(new_data)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_input.delete(0, tk.END)
            username_or_email_input.delete(0, tk.END)
            username_or_email_input.insert(0, 'user@gmail.com')
            password_input.delete(0, tk.END)


# ----------------------------  SEARCH ------------------------------- #

def find_account():
    """Searches through 'data.json' for matching results.
    If there is a match — shows a pop-up with account details: Website Name, Username, Password."""
    searched_website = website_input.get()
    if len(searched_website) == 0:
        messagebox.showerror(message="To perform 'Search' you need to write down a website name.")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
                username = data[searched_website]['username']
                password = data[searched_website]['password']
        except KeyError:
            messagebox.showinfo(title="Info", message=f"No matches")
        except FileNotFoundError:
            messagebox.showinfo(title="Info", message=f"Data file missing.\nThere are no accounts created yet.")
        else:
            messagebox.showinfo(title="Info", message=f"Website: {searched_website}\nUser: {username}\nPassword: {password}")


# ---------------------------- UI SETUP ------------------------------- #

window = tk.Tk()
window.title("Password Manager")
window.config(padx=64, pady=64)

# Row 0
logo_image = tk.PhotoImage(file='logo.png')
canvas = tk.Canvas(width=240, height=200)
canvas.create_image(120, 100, image=logo_image)
canvas.grid(column=1, row=0)

# Row 1
website_label = tk.Label(text='Website:')
website_label.grid(column=0, row=1)

website_input = tk.Entry(width=27)
website_input.focus()
website_input.grid(column=1, row=1, columnspan=1)

btn_search = tk.Button(text='Search', width=6, command=find_account)
btn_search.grid(column=2, row=1)

# Row 2
username_or_email_label = tk.Label(text='Email/Username:')
username_or_email_label.grid(column=0, row=2)

username_or_email_input = tk.Entry(width=27)
username_or_email_input.insert(0, 'user@gmail.com')
username_or_email_input.grid(column=1, row=2, columnspan=1)

# Row 3
password_label = tk.Label(text='Password:')
password_label.grid(column=0, row=3)

password_input = tk.Entry(width=27)
password_input.grid(column=1, row=3)

btn_generate_password = tk.Button(text='Generate', width=6, command=generate_password)
btn_generate_password.grid(column=2, row=3)

# Row 4
btn_add = tk.Button(text='Add', width=36, command=save)
btn_add.grid(column=1, row=4, columnspan=2)

window.mainloop()

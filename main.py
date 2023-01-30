from tkinter import *
from tkinter import messagebox
import random
import string
import pyperclip
import json


# def messageWindow():
#     win = Toplevel()
#     win.title('warning')
#     message = "This will delete stuff"
#     Label(win, text=message).pack()
#     Button(win, text='Delete', command=win.destroy).pack()

# ---------------------------- DELETE PASSWORD ------------------------------- #
def delete():
    website = website_input.get().lower()
    try:
        with open("data.json", 'r') as file:
            # Reading old data
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="Oops", message=f"There is no such record as '{website}'")
    else:
        if website in data:
            delete_record = messagebox.askyesno(title=website,
                                message=f"Are you sure to delete this record?\nWebsite: {website}\nEmail: {data[website]['email']}\nPassword: {data[website]['password']}")
            if delete_record:
                del data[website]
                with open("data.json", 'w') as file:
                    # Saving updated data
                    json.dump(data, file, indent=4)
        else:
            messagebox.showinfo(title="Oops", message=f"There is no such record as '{website}'")


# ---------------------------- SEARCH PASSWORD ------------------------------- #
def search():
    website = website_input.get().lower()
    try:
        with open("data.json", 'r') as file:
            # Reading old data
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="Oops", message=f"There is no such record as '{website}'")
    else:
        if website in data:
            messagebox.showinfo(title=website,
                                message=f"Website: {website}\nEmail: {data[website]['email']}\nPassword: {data[website]['password']}")
        else:
            messagebox.showinfo(title="Oops", message=f"There is no such record as '{website}'")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_pass():
    random_password = ''.join(
        [random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(12)])
    password_input.delete(0, END)
    password_input.insert(0, random_password)
    pyperclip.copy(random_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()
    new_data = {
        website.lower(): {
            "email": email.lower(),
            "password": password,
        }
    }
    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops",
                            message="Don't leave empty fields!")
    else:
        is_ok = messagebox.askokcancel(title=website,
                                       message=f"Is this data correct?\nWebsite: {website}\nEmail: {email}\nPassword: {password}")
        if is_ok:
            try:
                with open("data.json", 'r') as file:
                    # Reading old data
                    data = json.load(file)
                    # Updating old data with new data
                    data.update(new_data)
            except FileNotFoundError:
                with open("data.json", 'w') as file:
                    # Saving updated data
                    json.dump(new_data, file, indent=4)
            else:
                with open("data.json", 'w') as file:
                    # Saving updated data
                    json.dump(data, file, indent=4)
            website_input.delete(0, END)
            password_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
root = Tk()
root.config(padx=60, pady=60, bg="white")
root.title("Password Manager")
canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
bg_photo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=bg_photo)
canvas.grid(row=0, column=1, columnspan=2, sticky="w")

website_label = Label(text="Website:", bg="white")
website_label.grid(row=1, column=0)

email_label = Label(text="Email/Username:", bg="white")
email_label.grid(row=2, column=0)

password_label = Label(text="Password:", bg="white")
password_label.grid(row=3, column=0)

website_input = Entry(width=34)
website_input.focus()
website_input.grid(row=1, column=1, columnspan=2, sticky="w")

email_input = Entry(width=43)
email_input.insert(0, "m.ociepka97@gmail.com")
email_input.grid(row=2, column=1, columnspan=2, sticky="w")

password_input = Entry(width=24)
password_input.grid(row=3, column=1, sticky="w")

button_add = Button(text='Add', command=add, width=36)
button_add.grid(row=4, column=1, columnspan=2, sticky="w", pady=10)

button_generate_pass = Button(text='Generate Password', command=generate_pass)
button_generate_pass.grid(row=3, column=2, sticky="e")

button_search = Button(text='Search', command=search)
button_search.grid(row=1, column=2, sticky="e")

button_delete = Button(text='Delete', command=delete, width=36)
button_delete.grid(row=5, column=1, columnspan=2, sticky="w")

# button_message = Button(text='Bring up Message', command=messageWindow)
# button_message.grid(row=5, column=1, sticky="e")

root.mainloop()

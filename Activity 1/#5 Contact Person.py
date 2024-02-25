import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import math
import re
def add_person():
    name = name_entry.get()
    number = phone_entry.get()

    # Validating the phone number
    if not re.match(r'^09\d{9}$', number):
        messagebox.showerror("Invalid Phone Number", "Please enter a valid phone number.")
        phone_entry.delete(0, tk.END)
        return

    try:
        with open("contacts.txt", "r") as file:
            for line in file:
                contact = line.strip().split(",")
                if contact[0] == name:
                    messagebox.showerror("Duplicate Entry", "The name already exists.")
                    return
                if contact[1] == number:
                    messagebox.showerror("Duplicate Entry", "The phone number already exists.")
                    return

        with open("contacts.txt", "a") as file:
            file.write(f"{name},{number}\n")
        messagebox.showinfo("Person Added", f"{name} has been added to the contact list.")

    except FileNotFoundError:
        messagebox.showerror("File Not Found", "The contacts file does not exist.")

    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)

def find_person():
    number = find_phone.get()
    found = False

    # Check if the phone number is a valid 11-digit positive integer
    if not re.match(r'^09\d{9}$', number):
        messagebox.showerror("Invalid Phone Number", "Please enter a valid 11-digit positive integer starting with '09' for the phone number.")
        find_phone.delete(0, tk.END)
        return

    try:
        with open("contacts.txt", "r") as file:
            for line in file:
                contact = line.strip().split(",")
                if contact[1] == number:
                    name = contact[0]
                    messagebox.showinfo("Person Found", f"The person with phone number {number} is {name}.")
                    found = True
                    break

        if not found:
            messagebox.showinfo("Person Not Found", f"No person found with phone number {number}.")

    except FileNotFoundError:
        messagebox.showerror("File Not Found", "The contacts file does not exist.")

    find_phone.delete(0, tk.END)

# Creating the main window
window = tk.Tk()
window.title("Contact Search")
width = window.winfo_screenwidth()
height = window.winfo_screenheight()
w = 400
h = 280
x = math.floor((width - w) / 2)
y = math.floor((height - h) / 2)
window.geometry(f"{w}x{h}+{x}+{y}")

# Creating add person section
style = ttk.Style()
style.configure("Bold.TLabel", font=("Arial", 12, "bold"))

add_label = ttk.Label(window, text="Add Person", style="Bold.TLabel")
add_label.pack()

add_name = ttk.Label(window, text="Name:")
add_name.pack()
name_entry = tk.Entry(window)
name_entry.pack()

add_phone = ttk.Label(window, text="Phone Number:")
add_phone.pack()
phone_entry = tk.Entry(window)
phone_entry.pack()

add_person = ttk.Button(window, text="Add Person", command=add_person)
add_person.pack()
space = ttk.Label(window, text="")
space.pack()

# Creating find person section
find_label = ttk.Label(window, text="Find Person", style="Bold.TLabel")
find_label.pack()

find_phone_label = ttk.Label(window, text="Phone Number:")
find_phone_label.pack()
find_phone = tk.Entry(window)
find_phone.pack()

find_person = ttk.Button(window, text="Find Person", command=find_person)
find_person.pack()

space2 = ttk.Label(window, text='')
space2.pack()
exit = ttk.Button(window, text="Exit", command=window.quit)
exit.pack()

window.mainloop()
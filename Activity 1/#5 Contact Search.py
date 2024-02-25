import tkinter as tk
from tkinter import messagebox
import re
import os

class Contact:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Contact Search")
        width = self.window.winfo_screenwidth()
        height = self.window.winfo_screenheight()
        w = (width - 600) // 2
        h = (height - 400) // 2
        self.window.geometry(f"{600}x{400}+{w}+{h}")

        self.button_color = "#007bff"
        self.button_text_color = "white"
        self.label_color1 = "#007bff"
        self.label_text_color1 = "white"
        self.label_color2 = "#d1ecf1"
        self.label_text_color2 = "#2d7588"
        self.label_color3 = "white"
        self.label_text_color3 = "#007bff"
        self.label_color4 = "#e8f0fe"

        self.bg_img = tk.PhotoImage(file="bg.png")
        self.bg_label = tk.Label(self.window, image=self.bg_img)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.create_widgets()

    def create_widgets(self):
        frame = tk.Frame(self.window, bg="white")
        frame.place(relx=0.5, rely=0.5, anchor="center")

        title = tk.Label(self.window, text="Contact Search System", bg=self.label_color1, fg=self.label_text_color1, font=("Helvetica", 14, "bold"))
        title.pack(fill="x")

        add_label = tk.Label(frame, text="Add Person", bg=self.label_color3, fg=self.label_text_color3, font=("Helvetica", 13))
        add_label.pack(pady=10)

        add_name = tk.Label(frame, text="Name:", bg=self.label_color2, fg=self.label_text_color2, font=("Helvetica", 11))
        add_name.pack()
        self.name_entry = tk.Entry(frame, bg=self.label_color4, font=("Helvetica", 11))
        self.name_entry.pack()

        add_phone = tk.Label(frame, text="Phone Number:", bg=self.label_color2, fg=self.label_text_color2, font=("Helvetica", 11))
        add_phone.pack()
        self.phone_entry = tk.Entry(frame, bg=self.label_color4, font=("Helvetica", 11))
        self.phone_entry.pack()

        add_person = tk.Button(frame, text="Add Person", bg=self.button_color, fg=self.button_text_color, font=("Helvetica", 11), command=self.add_person)
        add_person.pack(pady=(10, 5))

        find_label = tk.Label(frame, text="Find Person", bg=self.label_color3, fg=self.label_text_color3, font=("Helvetica", 13))
        find_label.pack(pady=10)

        find_phone_label = tk.Label(frame, text="Phone Number:", bg=self.label_color2, fg=self.label_text_color2, font=("Helvetica", 11))
        find_phone_label.pack()
        self.find_phone = tk.Entry(frame, bg=self.label_color4, font=("Helvetica", 11))
        self.find_phone.pack()

        find_person = tk.Button(frame, text="Find Person", bg=self.button_color, fg=self.button_text_color, font=("Helvetica", 11), command=self.find_person)
        find_person.pack(pady=(10, 5))

        exit_button = tk.Button(frame, text="Exit", bg=self.button_color, fg=self.button_text_color, font=("Helvetica", 11), command=self.window.destroy)
        exit_button.pack(pady=10)

    def add_person(self):
        name = self.name_entry.get()
        number = self.phone_entry.get()

        if not re.match(r'^09\d{9}$', number):
            messagebox.showerror("Invalid Phone Number", "Please enter a valid phone number.")
            self.phone_entry.delete(0, tk.END)
            return

        try:
            if not os.path.exists("contacts.txt"):
                open("contacts.txt", "w").close()

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

        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)

    def find_person(self):
        number = self.find_phone.get()
        found = False

        if not re.match(r'^09\d{9}$', number):
            messagebox.showerror("Invalid Phone Number", "Please enter a valid phone number.")
            self.find_phone.delete(0, tk.END)
            return

        try:
            if not os.path.exists("contacts.txt"):
                open("contacts.txt", "w").close()

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

        self.find_phone.delete(0, tk.END)

def main():
    app = Contact()
    app.window.mainloop()

if __name__ == "__main__":
    main()
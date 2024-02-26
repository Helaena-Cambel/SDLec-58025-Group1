import tkinter as tk
from tkinter import simpledialog, messagebox

class Inventory:
    def __init__(self, master):
        self.master = master
        self.master.title("Inventory Management System")
        width = self.master.winfo_screenwidth()
        height = self.master.winfo_screenheight()
        w = (width - 600) // 2
        h = (height - 400) // 2
        self.master.geometry(f"{600}x{400}+{w}+{h}")

        self.button_color = "#007bff"
        self.button_text_color = "white"
        self.label_color = "#007bff"
        self.label_text_color = "#ffffff"

        self.inventory = {
            "Motherboards": 0,
            "Hard Disks": 0,
            "Diskettes": 0,
            "Compact Disks": 0,
            "Memory Cards": 0
        }

        # Load background image
        self.bg_img = tk.PhotoImage(file="bg.png")
        self.bg_label = tk.Label(self.master, image=self.bg_img)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.create_widgets()

    def create_widgets(self):
        font_style = ("Helvetica", 12)

        title_label = tk.Label(self.master, text="Inventory Management System", bg=self.label_color, fg=self.label_text_color, font=("Helvetica", 14, "bold"))
        title_label.pack(fill="x", pady=(10, 5))

        self.display_frame = tk.LabelFrame(self.master, text="Inventory", font=font_style, bd=10, relief="ridge")
        self.display_frame.pack(padx=10, pady=5)

        self.inventory_listbox = tk.Listbox(self.display_frame, width=30, font=font_style, borderwidth=0, highlightthickness=0)
        self.inventory_listbox.pack(padx=5, pady=5)

        self.update_inventory_display()

        self.menu_frame = tk.LabelFrame(self.master, text="Menu", font=font_style, bd=5, relief="ridge")
        self.menu_frame.pack(padx=10, pady=5)

        button_style = ("Helvetica", 12, "bold")

        self.add_button = tk.Button(self.menu_frame, text="Add Items", command=self.add_items, bg=self.button_color, fg=self.button_text_color, font=button_style)
        self.add_button.grid(row=0, column=0, padx=5, pady=5)

        self.remove_button = tk.Button(self.menu_frame, text="Remove Items", command=self.remove_items, bg=self.button_color, fg=self.button_text_color, font=button_style)
        self.remove_button.grid(row=0, column=1, padx=5, pady=5)

        self.quit_button = tk.Button(self.menu_frame, text="Quit", command=self.master.quit, bg=self.button_color, fg=self.button_text_color, font=button_style)
        self.quit_button.grid(row=0, column=2, padx=5, pady=5)

    def add_items(self):
        item = self.select_item()
        if item:
            quantity = self.get_quantity()
            if quantity:
                self.inventory[item] += quantity
                self.update_inventory_display()

    def remove_items(self):
        item = self.select_item()
        if item:
            quantity = self.get_quantity()
            if quantity:
                if self.inventory[item] >= quantity:
                    self.inventory[item] -= quantity
                    self.update_inventory_display()
                else:
                    messagebox.showwarning("Warning", "Insufficient quantity in inventory.")

    def select_item(self):
        if self.inventory_listbox.curselection():
            return self.inventory_listbox.get(self.inventory_listbox.curselection()).split(":")[0]
        else:
            messagebox.showwarning("Warning", "Please select an item.")
            return None

    def get_quantity(self):
        try:
            quantity = int(simpledialog.askstring("Quantity", "Enter quantity:"))
            if quantity <= 0:
                messagebox.showerror("Error", "Quantity must be a positive integer.")
                return None
            return quantity
        except ValueError:
            messagebox.showerror("Error", "Invalid quantity.")
            return None

    def update_inventory_display(self):
        self.inventory_listbox.delete(0, tk.END)
        for item, quantity in self.inventory.items():
            self.inventory_listbox.insert(tk.END, f"{item}: {quantity}")


def main():
    root = tk.Tk()
    root.geometry("500x500")
    app = Inventory(root)
    root.mainloop()

if __name__ == "__main__":
    main()

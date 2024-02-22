import tkinter as tk
from tkinter import simpledialog, messagebox

class Inventory:
    def __init__(self, masterlist):
        self.masterlist = masterlist
        self.masterlist.title("Inventory Management System")

        self.inventory = {
            "Motherboards": 0,
            "Hard Disks": 0,
            "Diskettes": 0,
            "Compact Disks": 0,
            "Memory Cards": 0
        }

        self.create_widgets()

    def create_widgets(self):
        self.display_frame = tk.LabelFrame(self.masterlist, text="Inventory")
        self.display_frame.pack(padx=10, pady=10)

        self.inventory_listbox = tk.Listbox(self.display_frame, width=30, height=10)
        self.inventory_listbox.pack(padx=5, pady=5)

        for item, quantity in self.inventory.items():
            self.inventory_listbox.insert(tk.END, f"{item}: {quantity}")

        self.menu_frame = tk.LabelFrame(self.masterlist, text="Menu")
        self.menu_frame.pack(padx=10, pady=10)

        self.add_button = tk.Button(self.menu_frame, text="Add Items", command=self.add_items)
        self.add_button.grid(row=0, column=0, padx=5, pady=5)

        self.remove_button = tk.Button(self.menu_frame, text="Remove Items", command=self.remove_items)
        self.remove_button.grid(row=0, column=1, padx=5, pady=5)

        self.quit_button = tk.Button(self.menu_frame, text="Quit", command=self.masterlist.quit)
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
    app = Inventory(root)
    root.mainloop()


if __name__ == "__main__":
    main()

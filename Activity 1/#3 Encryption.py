import tkinter as tk
from tkinter import ttk

def encrypt_text():
    letters = ("abcdefghijklmnopqrstuvwxyz"
               "ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    random = in_text.get()

    # Encrypting the text input
    encrypted = ""
    for char in random:
        if char in letters:
            idx = letters.find(char)
            shift = (idx + 1) % len(letters)
            if char == 'z':
                encrypted_char = 'a'
            elif char == 'Z':
                encrypted_char = 'A'
            else:
                encrypted_char = letters[shift]
            encrypted += encrypted_char
        else:
            encrypted += char

    out_text.set("Encrypted: " + encrypted)

# Creating the main window
window = tk.Tk()
window.title("Text Encryption")
width = window.winfo_screenwidth()
height = window.winfo_screenheight()
w = (width - 400) // 2
h = (height - 200) // 2
window.geometry(f'400x200+{w}+{h}')

# Creating input label and text input
in_label = ttk.Label(window, text="Input text to encrypt:")
in_label.pack()
in_text = ttk.Entry(window)
in_text.pack()

# Creating encrypt button
encrypt_button = ttk.Button(window, text="Encrypt", command=encrypt_text)
encrypt_button.pack()

# Creating output label
out_text = tk.StringVar()
out_label = ttk.Label(window, textvariable=out_text)
out_label.pack()
space1 = ttk.Label(window, text='')
space1.pack()

# Creating clear and exit button
clear = ttk.Button(window, text="Clear", command=lambda: (in_text.delete(0, tk.END), out_text.set("")))
clear.pack()
space2 = ttk.Label(window, text='')
space2.pack()
exit = ttk.Button(window, text="Exit", command=window.quit)
exit.pack()

window.mainloop()
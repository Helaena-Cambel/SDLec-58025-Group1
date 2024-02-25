import tkinter as tk

class Encrypt:
    def __init__(self, window):
        self.window = window
        self.window.title("Text Encryption")
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

        title = tk.Label(self.window, text="Text Encryption System", bg=self.label_color1, fg=self.label_text_color1, font=("Helvetica", 14, "bold"))
        title.pack(fill="x", pady=(10, 5))

        input_label = tk.Label(frame, text="Enter text to encrypt:", bg=self.label_color2, fg=self.label_text_color2, font=("Helvetica", 12))
        input_label.pack(pady=(20, 10))

        self.input_text = tk.Entry(frame, bg=self.label_color4, font=("Helvetica", 12))
        self.input_text.pack()

        encrypt_button = tk.Button(frame, text="Encrypt", bg=self.button_color, fg=self.button_text_color, font=("Helvetica", 12), command=self.encrypt_text)
        encrypt_button.pack(pady=(10, 5))

        self.output = tk.Label(frame, text="", bg=self.label_color3, fg=self.label_text_color3, font=("Helvetica", 12))
        self.output.pack(pady=(10, 30))

        clear_button = tk.Button(frame, text="Clear", bg=self.button_color, fg=self.button_text_color, font=("Helvetica", 12), command=self.clear_text)
        clear_button.pack(pady=5)

        exit_button = tk.Button(frame, text="Exit", bg=self.button_color, fg=self.button_text_color, font=("Helvetica", 12), command=self.window.destroy)
        exit_button.pack(pady=10)

    def encrypt_text(self):
        text = self.input_text.get()
        encrypted_text = ""

        for char in text:
            if char.isalpha():
                if char.islower():
                    encrypted_char = chr((ord(char) - ord('a') + 1) % 26 + ord('a'))
                else:
                    encrypted_char = chr((ord(char) - ord('A') + 1) % 26 + ord('A'))
            else:
                encrypted_char = char

            encrypted_text += encrypted_char

        self.output.config(text="Encrypted Text: " + encrypted_text)

    def clear_text(self):
        self.input_text.delete(0, tk.END)
        self.output.config(text="")

def main():
    root = tk.Tk()
    app = Encrypt(root)
    root.mainloop()

if __name__ == "__main__":
    main()
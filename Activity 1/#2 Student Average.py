import tkinter as tk
from tkinter import messagebox


class StudentGradesApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Student Average")
        width = self.master.winfo_screenwidth()
        height = self.master.winfo_screenheight()
        w = (width - 700) // 2
        h = (height - 50) // 2
        self.master.geometry(f"{700}x{500}+{w}+{h}")
        self.master.configure(bg="#e8f0fe")

        self.background_image = tk.PhotoImage(file="bg1.png")
        self.background_label = tk.Label(master, image=self.background_image)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.title_label = tk.Label(self.master, text="Student Average", font=("Arial", 18), bg="#007bff", fg="white")
        self.title_label.pack(pady=10)

        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()
        window_width = 600
        window_height = 400
        x = (screen_width / 2) - (window_width / 2)
        y = (screen_height / 2) - (window_height / 2)
        self.master.geometry('%dx%d+%d+%d' % (window_width, window_height, x, y))

        self.students = {}
        self.num_quizzes = 0

        self.create_widgets()

    def create_widgets(self):
        self.scrollable_frame = tk.Frame(self.master, bg="#e8f0fe")
        self.scrollable_frame.pack(fill="both", expand=True)

        self.canvas = tk.Canvas(self.scrollable_frame, bg="#e8f0fe")
        self.canvas.pack(side="left", fill="both", expand=True)

        self.scrollbar_y = tk.Scrollbar(self.scrollable_frame, orient="vertical", command=self.canvas.yview)
        self.scrollbar_y.pack(side="right", fill="y")

        self.scrollbar_x = tk.Scrollbar(self.master, orient="horizontal", command=self.canvas.xview)
        self.scrollbar_x.pack(side="bottom", fill="x")

        self.canvas.configure(yscrollcommand=self.scrollbar_y.set, xscrollcommand=self.scrollbar_x.set)
        self.canvas.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))

        self.inner_frame = tk.Frame(self.canvas, bg="#e8f0fe")
        self.canvas.create_window((0, 0), window=self.inner_frame, anchor="nw")

        self.num_students_label = tk.Label(self.inner_frame, text="Number of Students:", bg="#e8f0fe")
        self.num_students_label.grid(row=0, column=0)

        self.num_students_entry = tk.Entry(self.inner_frame)
        self.num_students_entry.grid(row=0, column=1)

        self.num_quizzes_label = tk.Label(self.inner_frame, text="Number of Quizzes:", bg="#e8f0fe")
        self.num_quizzes_label.grid(row=1, column=0)

        self.num_quizzes_entry = tk.Entry(self.inner_frame)
        self.num_quizzes_entry.grid(row=1, column=1)

        self.create_students_button = tk.Button(self.inner_frame, text="Enter", command=self.create_students,
                                                bg="#007bff", fg="white")
        self.create_students_button.grid(row=2, columnspan=2, pady=10)

    def create_students(self):
        try:
            num_students = int(self.num_students_entry.get())
            if num_students <= 0:
                raise ValueError("Number of students should be a positive integer.")

            self.num_quizzes = int(self.num_quizzes_entry.get())
            if self.num_quizzes <= 0:
                raise ValueError("Number of quizzes should be a positive integer.")
        except ValueError as e:
            messagebox.showerror("Error", str(e))
            return

        self.num_students_label.grid_forget()
        self.num_students_entry.grid_forget()
        self.num_quizzes_label.grid_forget()
        self.num_quizzes_entry.grid_forget()
        self.create_students_button.grid_forget()

        for i in range(1, num_students + 1):
            self.create_student_widgets(i)

        self.calculate_button = tk.Button(self.inner_frame, text="Calculate Average", command=self.calculate_averages,
                                          bg="#007bff", fg="white")
        self.calculate_button.grid(row=len(self.students) + 1, columnspan=2, pady=10)

    def create_student_widgets(self, index):
        student_frame = tk.Frame(self.inner_frame, bg="#e8f0fe")
        student_frame.grid(row=index, columnspan=2, pady=5)

        name_label = tk.Label(student_frame, text=f"Student {index} Name:", bg="#e8f0fe")
        name_label.grid(row=0, column=0)
        name_entry = tk.Entry(student_frame)
        name_entry.grid(row=0, column=1)

        quiz_labels = []
        quiz_entries = []
        for i in range(self.num_quizzes):
            quiz_label = tk.Label(student_frame, text=f"Quiz {i + 1}:", bg="#e8f0fe")
            quiz_label.grid(row=i + 1, column=0)
            quiz_entry = tk.Entry(student_frame)
            quiz_entry.grid(row=i + 1, column=1)
            quiz_labels.append(quiz_label)
            quiz_entries.append(quiz_entry)

        self.students[index] = {
            'name': name_entry,
            'quizzes': quiz_entries
        }

    def calculate_averages(self):
        try:
            result_text = "Student Average:\n"
            class_quiz_totals = [0] * self.num_quizzes
            for student_index, student_data in self.students.items():
                student_name = student_data['name'].get().strip()
                student_quizzes = [float(entry.get()) for entry in student_data['quizzes']]
                student_average = sum(student_quizzes) / self.num_quizzes
                result_text += f"Student {student_index}: {student_name}'s average: {student_average:.2f}\n"
                for i, grade in enumerate(student_quizzes):
                    class_quiz_totals[i] += grade

            result_text += "\nClass Average:\n"
            class_averages = [total / len(self.students) for total in class_quiz_totals]
            for i, avg in enumerate(class_averages):
                result_text += f"Quiz {i + 1} average: {avg:.2f}\n"

            result_window = tk.Toplevel(self.master)
            result_window.title("Averages Summary")

            # Set the background image
            background_image = tk.PhotoImage(file="bg1.png")
            background_label = tk.Label(result_window, image=background_image)
            background_label.place(x=0, y=0, relwidth=1, relheight=1)

            result_window.configure(bg="#e8f0fe")

            result_label = tk.Label(result_window, text=result_text, font=("Arial", 12), bg="#e8f0fe")
            result_label.pack(padx=10, pady=10)

        except ValueError:
            messagebox.showerror("Error", "Please enter valid grades.")


def main():
    root = tk.Tk()
    app = StudentGradesApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()

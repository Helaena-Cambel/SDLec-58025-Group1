import tkinter as tk
import tkinter as ttk

class StudentGradesApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Student Grades App")

        self.num_students = 0
        self.num_quizzes = 0
        self.grades = {}

        self.create_widgets()

    def create_widgets(self):
        # Entry for number of students
        self.num_students_label = ttk.Label(self.master, text="Number of Students:")
        self.num_students_label.grid(row=0, column=0)
        self.num_students_entry = tk.Entry(self.master)
        self.num_students_entry.grid(row=0, column=1)

        # Button to enter number of students
        self.enter_students_button = ttk.Button(self.master, text="Enter", command=self.enter_students)
        self.enter_students_button.grid(row=0, column=2)

    def enter_students(self):
        self.num_students = int(self.num_students_entry.get())

        # Create entry fields for student names
        self.student_name_labels = []
        self.student_name_entries = []
        for i in range(self.num_students):
            label = ttk.Label(self.master, text=f"Student {i+1} Name:")
            label.grid(row=i+1, column=0, sticky='e')
            entry = tk.Entry(self.master)
            entry.grid(row=i+1, column=1)
            self.student_name_labels.append(label)
            self.student_name_entries.append(entry)

        # Button to enter quiz grades
        self.enter_grades_button = ttk.Button(self.master, text="Enter Grades", command=self.enter_grades)
        self.enter_grades_button.grid(row=self.num_students+1, column=0, columnspan=3)

    def enter_grades(self):
        self.num_quizzes = int(self.num_students_entry.get())

        # Get student names and create entry fields for quiz grades
        self.student_names = [entry.get() for entry in self.student_name_entries]

        self.quiz_grade_labels = []
        self.quiz_grade_entries = []
        for i in range(self.num_students):
            for j in range(self.num_quizzes):
                label = ttk.Label(self.master, text=f"Quiz {j+1} for {self.student_names[i]}:")
                label.grid(row=i+1, column=j+2, sticky='e')
                entry = tk.Entry(self.master)
                entry.grid(row=i+1, column=j+3)
                self.quiz_grade_labels.append(label)
                self.quiz_grade_entries.append(entry)

        # Button to calculate averages
        self.calculate_button = ttk.Button(self.master, text="Calculate Averages", command=self.calculate_averages)
        self.calculate_button.grid(row=self.num_students+2, column=0, columnspan=self.num_quizzes+4)

    def calculate_averages(self):
        # Get quiz grades for each student
        self.grades = {}
        for i in range(self.num_students):
            grades = []
            for j in range(self.num_quizzes):
                grade = float(self.quiz_grade_entries[i*self.num_quizzes + j].get())
                grades.append(grade)
            self.grades[self.student_names[i]] = grades

        # Compute student averages
        student_averages = {}
        for student, grades in self.grades.items():
            student_averages[student] = sum(grades) / len(grades)

        # Compute class averages for each quiz
        class_averages = [sum(self.grades[student][i] for student in self.grades) / self.num_students for i in range(self.num_quizzes)]

        # Display results
        result_window = tk.Toplevel(self.master)
        result_window.title("Results")

        result_text = "Individual Quiz Grades:\n"
        for student, grades in self.grades.items():
            result_text += f"{student}: {grades}\n"

        result_text += "\nAverage of Each Student in the Class:\n"
        for student, average in student_averages.items():
            result_text += f"{student}: {average:.2f}\n"

        result_text += "\nClass Average for Each Quiz:\n"
        for i, average in enumerate(class_averages):
            result_text += f"Quiz {i+1}: {average:.2f}\n"

        result_label = ttk.Label(result_window, text=result_text)
        result_label.pack()

def main():
    root = tk.Tk()
    app = StudentGradesApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()

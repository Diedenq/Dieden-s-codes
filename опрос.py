from tkinter.messagebox import showerror, showwarning, showinfo
import tkinter as tk

class SurveyApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Опросник")

        self.question_label = tk.Label(master, text="Как вы оцениваете этот опросник?")
        self.question_label.pack()

        self.scale_var = tk.IntVar()
        self.scale = tk.Scale(master, from_=1, to=5, orient=tk.HORIZONTAL, variable=self.scale_var)
        self.scale.pack()

        self.submit_button = tk.Button(master, text="Отправить", command=self.submit_survey)
        self.submit_button.pack()

    def submit_survey(self):
        ratting = self.scale_var.get()
        feedback_message = f"Спасибо за вашу оценку: {ratting}"
        tk.messagebox.showinfo("Спасибо!", feedback_message)

if __name__ == "__main__":
    root = tk.Tk()
    app = SurveyApp(root)
    root.mainloop()
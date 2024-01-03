import tkinter as tk

def on_button_click():
    label.config(text="Привет, " + entry.get())

root = tk.Tk()
root.title("Пример с Tkinter")

label = tk.Label(root, text="Введите Ваше имя:")
entry = tk.Entry(root)
button = tk.Button(root, text="Привет!", command=on_button_click)

label.pack(pady=10)
entry.pack(pady=10)
button.pack(pady=10)

root.mainloop()
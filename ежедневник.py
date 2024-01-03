import tkinter as tk
from tkinter import messagebox

def save_entry():
    entry_text = entry.get()
    if entry_text:
        with open("Ежедневник.txt", "a") as file:
            file.write(entry_text + "\n")
        entry.delete(0, tk.END)
        messagebox.showinfo("Сохранено", "Запись сохранена успешно!")

def read_entries():
    try:
        with open("Ежедневник.txt", "r") as file:
            entries = file.readlines()
        entries_text = "\n".join(entries)
        messagebox.showinfo("Записи", entries_text)
    except FileNotFoundError:
        messagebox.showinfo("Файл не найден", "Еще нет сохраненных записей.")

root = tk.Tk()
root.title("Ежедневник")

entry = tk.Entry(root, width=50)
entry.pack(pady=10)

save_button = tk.Button(root, text="Сохранить", command=save_entry)
save_button.pack(pady=5)

read_button = tk.Button(root, text="Читать записи", command=read_entries)
read_button.pack(pady=5)

root.mainloop

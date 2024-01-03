import tkinter as tk
from tkinter import messagebox

def calculate_result():
    try:
        x = float(entry.get())

        if x == 0:
            raise ZeroDivisionError("Деление на ноль невозможно.")
        
        result = 10 / x

        result_label.config(text=f"Результат: {result}")

    except ValueError:
        messagebox.showerror("Ошибка", "Введите числовое значение.")

    except ZeroDivisionError as e:
        messagebox.showerror("Ошибка", str(e))

    except Exception as e:
        messagebox.showerror("Ошибка", f"Произошла ошибка: {e}")

root = tk.Tk()
root.title("Калькулятор")

entry = tk.Entry(root, width=20)
entry.pack(pady=10)

calculate_button = tk.Button(root, text="Рассчитать", command=calculate_result)
calculate_button.pack()

result_label = tk.Label(root, text="")
result_label.pack(pady=10)

root.mainloop()
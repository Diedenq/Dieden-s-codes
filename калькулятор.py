import tkinter as tk

def on_click(button_value):
    current = entry_var.get()
    if button_value == "=":
        try:
            result = eval(current)
            entry_var.set(result)
        except:
            entry_var.set("Ошибка")
    elif button_value == "C":
        entry_var.set("")
    else:
        entry_var.set(current + button_value)

window = tk.Tk()
window.title("Калькулятор")

entry_var = tk.StringVar()
entry = tk.Entry(window, textvariable=entry_var, font=("Arial", 14), justify="right")
entry.grid(row=0, column=0, columnspan=4)
# Кнопки калькулятора
buttons = [
"7", "8", "9", "+",
"4", "5", "6", "-",
"1", "2", "3", "*",
"0", ".", "=", "/",
"C"
]

row_val = 1
col_val = 0

for button in buttons:
    tk.Button(window, text=button, padx=20, pady=20, font=('Arial', 14), 
              command=lambda button=button: on_click(button)).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

window.mainloop()
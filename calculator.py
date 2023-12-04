import tkinter as tk

def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(number))

def clear():
    entry.delete(0, tk.END)

def add():
    first_number = entry.get()
    global f_num
    global math
    math = "addition"
    f_num = float(first_number)
    entry.delete(0, tk.END)

def subtract():
    first_number = entry.get()
    global f_num
    global math
    math = "subtraction"
    f_num = float(first_number)
    entry.delete(0, tk.END)

def multiply():
    first_number = entry.get()
    global f_num
    global math
    math = "multiplication"
    f_num = float(first_number)
    entry.delete(0, tk.END)

def divide():
    first_number = entry.get()
    global f_num
    global math
    math = "division"
    f_num = float(first_number)
    entry.delete(0, tk.END)

def equals():
    second_number = entry.get()
    entry.delete(0, tk.END)
    if math == "addition":
        entry.insert(0, f_num + float(second_number))
    if math == "subtraction":
        entry.insert(0, f_num - float(second_number))
    if math == "multiplication":
        entry.insert(0, f_num * float(second_number))
    if math == "division":
        entry.insert(0, f_num / float(second_number))

def on_key(event):
    if event.keysym.isdigit():
        button_click(event.keysym)
    elif event.keysym == "Return":
        equals()

# Створення вікна
root = tk.Tk()
root.title("Калькулятор")

# Введення для виразу
entry = tk.Entry(root, width=30, font=("Arial", 16, "bold"))
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
entry.bind("<Key>", on_key)

# Розміри кнопок
button_width = 10
button_height = 4

# Відступ між рядками та стовбцями
row_padding = 5
column_padding = 5

# Кнопки для цифр
button_1 = tk.Button(root, text="1", width=button_width, height=button_height, font=("Arial", 16, "bold"), command=lambda: button_click(1))
button_2 = tk.Button(root, text="2", width=button_width, height=button_height, font=("Arial", 16, "bold"), command=lambda: button_click(2))
button_3 = tk.Button(root, text="3", width=button_width, height=button_height, font=("Arial", 16, "bold"), command=lambda: button_click(3))
button_4 = tk.Button(root, text="4", width=button_width, height=button_height, font=("Arial", 16, "bold"), command=lambda: button_click(4))
button_5 = tk.Button(root, text="5", width=button_width, height=button_height, font=("Arial", 16, "bold"), command=lambda: button_click(5))
button_6 = tk.Button(root, text="6", width=button_width, height=button_height, font=("Arial", 16, "bold"), command=lambda: button_click(6))
button_7 = tk.Button(root, text="7", width=button_width, height=button_height, font=("Arial", 16, "bold"), command=lambda: button_click(7))
button_8 = tk.Button(root, text="8", width=button_width, height=button_height, font=("Arial", 16, "bold"), command=lambda: button_click(8))
button_9 = tk.Button(root, text="9", width=button_width, height=button_height, font=("Arial", 16, "bold"), command=lambda: button_click(9))
button_0 = tk.Button(root, text="0", width=button_width, height=button_height, font=("Arial", 16, "bold"), command=lambda: button_click(0))

# Кнопки для операцій
button_add = tk.Button(root, text="+", width=button_width, height=button_height, font=("Arial", 16, "bold"), command=add)
button_subtract = tk.Button(root, text="-", width=button_width, height=button_height, font=("Arial", 16, "bold"), command=subtract)
button_multiply = tk.Button(root, text="*", width=button_width, height=button_height, font=("Arial", 16, "bold"), command=multiply)
button_divide = tk.Button(root, text="/", width=button_width, height=button_height, font=("Arial", 16, "bold"), command=divide)
button_equal = tk.Button(root, text="=", width=button_width, height=button_height, font=("Arial", 16, "bold"), command=equals)
button_clear = tk.Button(root, text="Clear", width=button_width, height=button_height, font=("Arial", 16, "bold"), command=clear)

# Розміщення кнопок на вікні з відступами
button_1.grid(row=1, column=0, padx=column_padding, pady=row_padding)
button_2.grid(row=1, column=1, padx=column_padding, pady=row_padding)
button_3.grid(row=1, column=2, padx=column_padding, pady=row_padding)
button_4.grid(row=2, column=0, padx=column_padding, pady=row_padding)
button_5.grid(row=2, column=1, padx=column_padding, pady=row_padding)
button_6.grid(row=2, column=2, padx=column_padding, pady=row_padding)
button_7.grid(row=3, column=0, padx=column_padding, pady=row_padding)
button_8.grid(row=3, column=1, padx=column_padding, pady=row_padding)
button_9.grid(row=3, column=2, padx=column_padding, pady=row_padding)
button_0.grid(row=4, column=1, padx=column_padding, pady=row_padding)
button_add.grid(row=1, column=3, padx=column_padding, pady=row_padding)
button_subtract.grid(row=2, column=3, padx=column_padding, pady=row_padding)
button_multiply.grid(row=3, column=3, padx=column_padding, pady=row_padding)
button_divide.grid(row=4, column=3, padx=column_padding, pady=row_padding)
button_equal.grid(row=4, column=2, padx=column_padding, pady=row_padding)
button_clear.grid(row=4, column=0, padx=column_padding, pady=row_padding)

root.mainloop()
import tkinter as tk

window = tk.Tk()
window.title("Simple Calculator")

result_label = tk.Label(window, text="Enter numbers and choose an operation", font=("Arial", 12))
result_label.pack(pady=10)

frame = tk.Frame(window, bg="gray", padx=20, pady=20)
frame.pack()

label1 = tk.Label(frame, text="Enter 1st Number:", bg="gray")
label1.grid(row=0, column=0, padx=10, pady=10)

entry1 = tk.Entry(frame)
entry1.grid(row=0, column=1, padx=10, pady=10)

label2 = tk.Label(frame, text="Enter 2nd Number:", bg="gray")
label2.grid(row=1, column=0, padx=10, pady=10)

entry2 = tk.Entry(frame)
entry2.grid(row=1, column=1, padx=10, pady=10)

def add():
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    result_label.config(text=f"The sum of {num1} + {num2} is {num1 + num2}.")

def subtract():
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    result_label.config(text=f"The difference of {num1} - {num2} is {num1 - num2}.")

def multiply():
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    result_label.config(text=f"The product of {num1} * {num2} is {num1 * num2}.")

def divide():
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    result_label.config(text=f"The division of {num1} / {num2} is {num1 / num2}.")

btn_add = tk.Button(frame, text="Add", width=12, command=add)
btn_add.grid(row=2, column=0, pady=10)

btn_sub = tk.Button(frame, text="Subtract", width=12, command=subtract)
btn_sub.grid(row=2, column=1, pady=10)

btn_mul = tk.Button(frame, text="Multiply", width=12, command=multiply)
btn_mul.grid(row=3, column=0, pady=10)

btn_div = tk.Button(frame, text="Division", width=12, command=divide)
btn_div.grid(row=3, column=1, pady=10)

window.mainloop()
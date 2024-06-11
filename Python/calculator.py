# Calculator app
import tkinter as tk
import math
from tkinter import messagebox


# Logic
def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y


def power(x, y):
    return x ** y


def combination(n, r):
    return math.factorial(n) / (math.factorial(r) * math.factorial(n - r))


def permutation(n, r):
    return math.factorial(n) / math.factorial(n - r)


def to_binary(x):
    return bin(x)[2:]


def to_hex(x):
    return hex(x)[2:]


def clear():
    entry.delete(0, tk.END)


# Create a window
root = tk.Tk()
root.title("Calculator")

# Create a calculator screen
entry = tk.Entry(root, width=35, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)


# Define buttons
def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, str(current) + str(number))


# Create a calculator UI
button_1 = tk.Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
button_2 = tk.Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3 = tk.Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
button_4 = tk.Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5 = tk.Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 = tk.Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
button_7 = tk.Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8 = tk.Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9 = tk.Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
button_0 = tk.Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))

button_add = tk.Button(root, text="+", padx=52, pady=20, command=lambda: button_click("+"))
button_subtract = tk.Button(root, text="-", padx=55, pady=20, command=lambda: button_click("-"))
button_multiply = tk.Button(root, text="*", padx=52, pady=20, command=lambda: button_click("*"))
button_divide = tk.Button(root, text="/", padx=55, pady=20, command=lambda: button_click("/"))
button_power = tk.Button(root, text="^", padx=52, pady=20, command=lambda: button_click("**"))
button_clear = tk.Button(root, text="C", padx=52, pady=20, command=clear)

button_equal = tk.Button(root, text="=", padx=40, pady=20, command=lambda: button_click("="))
button_decimal = tk.Button(root, text=".", padx=40, pady=20, command=lambda: button_click("."))
button_combination = tk.Button(root, text="C(n, r)", padx=42, pady=20, command=lambda: button_click("C"))
button_permutation = tk.Button(root, text="P(n, r)", padx=42, pady=20, command=lambda: button_click("P"))
button_binary = tk.Button(root, text="Binary", padx=40, pady=20, command=lambda: button_click("Binary"))
button_hex = tk.Button(root, text="Hex", padx=50, pady=20, command=lambda: button_click("Hex"))

# Place buttons on the screen
button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_add.grid(row=1, column=3)
button_subtract.grid(row=1, column=4)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_multiply.grid(row=2, column=3)
button_divide.grid(row=2, column=4)
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_power.grid(row=3, column=3)
button_combination.grid(row=3, column=4)
button_permutation.grid(row=3, column=5)

button_0.grid(row=4, column=0)
button_decimal.grid(row=4, column=1)
button_equal.grid(row=4, column=2)
button_binary.grid(row=4, column=3)
button_hex.grid(row=4, column=4)
button_clear.grid(row=4, column=5)


# make buttons functional
def evaluate():
    try:
        expression = entry.get()

        if "+" in expression:
            x, y = expression.split("+")
            result = add(float(x), float(y))
        elif "-" in expression:
            x, y = expression.split("-")
            result = subtract(float(x), float(y))
        elif "*" in expression:
            x, y = expression.split("*")
            result = multiply(float(x), float(y))
        elif "/" in expression:
            x, y = expression.split("/")
            result = divide(float(x), float(y))
        elif "**" in expression:
            x, y = expression.split("**")
            result = power(float(x), float(y))
        elif "C" in expression:
            n, r = expression.split("C")
            result = combination(int(n), int(r))
        elif "P" in expression:
            n, r = expression.split("P")
            result = permutation(int(n), int(r))
        elif "Binary" in expression:
            x = expression.split("Binary")
            result = to_binary(int(x[0]))
        elif "Hex" in expression:
            x = expression.split("Hex")
            result = to_hex(int(x[0]))
        else:
            result = "Invalid input!"

        entry.delete(0, tk.END)
        entry.insert(0, result)


    except:
        messagebox.showerror("Error", "Invalid input!")
        entry.delete(0, tk.END)


button_equal.config(command=evaluate)

# run app
root.mainloop()

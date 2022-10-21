#!/usr/bin/env python3
import tkinter as tk
import math

window = tk.Tk()

weight_value = tk.IntVar()
height_value = tk.IntVar()

weight = tk.Label(window, text="please enter your weight in kg:", foreground="black", font="bold")
weight.grid(row=0, column=0)

height = tk.Label(window, text="please enter your height in cm:", foreground="black", font="bold")
height.grid(row=1, column=0)

weight_entered = tk.Entry(window, textvariable=weight_value)
weight_entered.grid(column=1, row=0)

height_entered = tk.Entry(window, textvariable=height_value)
height_entered.grid(column=1, row=1)


def calculate():
    result_calculated = int(weight_value.get()) / (int(height_value.get() / 100)**2)
    result.configure(text=float(result_calculated))


calculate_button = tk.Button(window, text="calculate", width=30, height=3, command=calculate)
calculate_button.grid(column=0, row=2)

result = tk.Label(window, text="BMI", foreground='red', font="bold")
result.grid(column=1, row=2)

window.mainloop()

#!/usr/bin/env python3
import tkinter as tk
from tkinter import ttk

# ttk provides access to the tk widget set

window = tk.Tk()

names = tk.StringVar()

combobox_one_picked_name = ttk.Combobox(window, width=20, textvariable=names, values=["john", "william", "bob", "anna"],
                                        state="readonly")
combobox_one_picked_name.current(0)  # picks the first name in the list
combobox_one_picked_name.grid(column=1, row=0)

ttk.Label(window, text="Pick a name: ", font=("Arial", 12, "italic", "bold")).grid(column=0, row=0)  # label 1


def show_name():
    chosen_show.configure(text=("Hello, " + names.get()))


chosen_show = ttk.Button(window, text="hello", command=show_name)
chosen_show.grid(column=1, row=1)

# radio button section below
chVarArr = tk.IntVar()
chVarRel = tk.IntVar()
chVarDec = tk.IntVar()

my_check = tk.Checkbutton(window, text="Arrest them", variable=chVarArr, state="disable")
my_check.grid(column=0, row=2, sticky=tk.W)

my_check2 = tk.Checkbutton(window, text="Release them", variable=chVarRel)
my_check2.grid(column=1, row=2, sticky=tk.W)

my_check3 = tk.Checkbutton(window, text="decide later", variable=chVarDec)
my_check3.grid(column=2, row=2, sticky=tk.W)  # sticky=w aligns to the west of the grid aka the left

my_check.deselect()
my_check2.deselect()
my_check3.select()

color1 = 'blue'
color2 = 'black'
color3 = 'red'


def radio_button_color_changer():
    radio_select = redVar.get()
    if radio_select == 1:
        window.configure(background=color1)
    elif radio_select == 2:
        window.configure(background=color2)
    elif radio_select == 3:
        window.configure(background=color3)


redVar = tk.IntVar()

radio1 = tk.Radiobutton(window, text=color1, variable=redVar, value=1, command=radio_button_color_changer)
radio1.grid(column=0, row=3, sticky=tk.W)

radio2 = tk.Radiobutton(window, text=color2, variable=redVar, value=2, command=radio_button_color_changer())
radio2.grid(column=1, row=3, sticky=tk.W)

radio3 = tk.Radiobutton(window, text=color3, variable=redVar, value=3, command=radio_button_color_changer)
radio3.grid(column=2, row=3, sticky=tk.W)

window.mainloop()

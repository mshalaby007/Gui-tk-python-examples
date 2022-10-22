#!/usr/bin/env python3
import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("OAK")

tab_control = ttk.Notebook(window)
tab1 = ttk.Frame(tab_control)
tab_control.add(tab1, text="Tab 1")
tab_control.pack(expand=1, fill="both")

tab2 = ttk.Frame(tab_control)
tab_control.add(tab2, text="Tab 2")

lab_fr_cont = ttk.LabelFrame(tab1,text="Label frame Controller")
lab_fr_cont.grid(column=0,row=0,padx=10,pady=5)

label1 = ttk.Label(lab_fr_cont,text="Enter a name: ")
label1.grid(column=0,row=0,sticky=tk.W)

ttk.Label(lab_fr_cont,text="choose a name").grid(column=1,row=0)

for child in lab_fr_cont.winfo_children():
    child.grid_configure(padx=10)

lab_fr_cont = ttk.LabelFrame(tab2,text="Label Frame 2")
lab_fr_cont.grid(column=0,row=0,padx=10,pady=5)

window.mainloop()

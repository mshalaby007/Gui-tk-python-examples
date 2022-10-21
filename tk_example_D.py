#!/usr/bin/env python3
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext

window = tk.Tk()
window.title("tk components")

scroll_w = 20
scroll_h = 5

# wrap=tk.WORD wraps based on words

scrText = scrolledtext.ScrolledText(window, wrap=tk.WORD, width=scroll_w, height=scroll_h)
scrText.grid(column=1, row=0, columnspan=3)

label1 = tk.Label(window,text="label 1").grid(column=0,row=0)
label2 = tk.Label(window,text="label 2").grid(column=0,row=1)
label3 = tk.Label(window,text="label 3").grid(column=0,row=2)

colors = ['blue','black','red']


def radio_button_color_changer():
    radio_select = redVar.get()
    if radio_select == 0:
        window.configure(background=colors[0])
    elif radio_select == 1:
        window.configure(background=colors[1])
    elif radio_select == 2:
        window.configure(background=colors[2])


redVar = tk.IntVar()

for col in range(3):
    cuRad = tk.Radiobutton(window,text=colors[col],variable=redVar,value=col,command=radio_button_color_changer)
    cuRad.grid(column=col,row=3,sticky=tk.W)


window.mainloop()

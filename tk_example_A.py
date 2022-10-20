#!/usr/bin/env python3
import tkinter as tk

window = tk.Tk()
window.title("First try")

label = tk.Label(window,text="hello python 1",foreground="red",background='blue',font='bold')
label.grid(column=0,row=0)#geometry method

# label2 = tk.Label(window,text="hello python 2",foreground="white",background="black")
# label2.grid(column=0,row=1)



#buttons <----
def resultOfButtonClick():
    buttonOne.configure(text="hello " + name.get())
    label.configure(foreground='black',text="something changed")

buttonOne = tk.Button(window,text="clickme",command=resultOfButtonClick)
buttonOne.grid(column=1,row=1)

name = tk.StringVar()#bound to the entry widget
text_widget = tk.Entry(window,width=20,textvariable=name)
text_widget.grid(column=0,row=1)

window.mainloop()

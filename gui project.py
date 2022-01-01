# -*- coding: utf-8 -*-
"""
Created on Sat Jan  1 12:42:25 2022

@author: DELL
"""

from tkinter import*
from tkinter import ttk
root=Tk()
root.geometry("900x900")
root.title("Dynamic GUI Elements")

new_Elements=["Label","Button","Dropdown"]
dropdown=ttk.Combobox(root, values=new_Elements)
dropdown.place(relx=0.5, rely=0.1, anchor=CENTER)

class Create_elements:
    def __init__(self):
        print("Create elements class")
    def create_label(self):
        label=Label(root, text="This label is created using a class")
        label.pack(padx=10, pady=10)
    def create_button(self):
        classbutton=Button(root, text="This button is created using a class", command=self.message)
        classbutton.pack(padx=10, pady=10)
    def create_dropdown(self):
        dropdown=ttk.Combobox(root, text="This dropdown is created using a function")
        dropdown.pack(padx=10, pady=10)
    def choose(self):
        global dropdown
        Element=dropdown.get()
        if (Element=="Label"):
            self.create_label()
        elif (Element=="Button"):
            self.create_button()
        elif (Element=="Dropdown"):
            self.create_dropdown()
    def message(self):
        messagebox.showinfo("show info", "U have clicked the button created using the class")

Object1=Create_elements()
button2=Button(root, text="click to create button and label", command=Object1.choose)
button2.pack(padx=10, pady=10)

























root.mainloop()
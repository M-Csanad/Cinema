from tkinter.ttk import *
import tkinter as tk
from ttkbootstrap.constants import *
import random
from tkinter import *
import ttkbootstrap as ttk


root = ttk.Window()
root.geometry("750x500")
root.resizable(False, False)
style =ttk.Style("vapor")



felirat = Label(root, text="Mozi", font=("Sans Sherif", 20))
terem1 = ttk.Button(root, text = "John Wick: 4. felvonás", style=LIGHT)
terem2 = ttk.Button(root, text = "Avatar: A víz útja", style=LIGHT)
terem3 = ttk.Button(root, text="SUPER MARIO BROS.: A FILM", style=LIGHT)
terem4 = ttk.Button(root, text="DUNGEONS & DRAGONS: BETYÁRBECSÜLET", style=LIGHT)
terem5 = ttk.Button(root, text="A BÁLNA", style=LIGHT)
terem6 = ttk.Button(root, text="A GALAXIS ŐRZŐI VOLUME 3.", style=LIGHT)

felirat.grid(column=1, row=0)
terem1.grid(column=0, row=1, padx=25, pady=20)
terem2.grid(column=1, row=1, padx=25, pady=20)
terem3.grid(column=2, row=1, padx=25, pady=20)
terem4.grid(column=0, row=2, padx=25, pady=20)
terem5.grid(column=1, row=2, padx=25, pady=20)
terem6.grid(column=2, row=2, padx=25, pady=20)
root.mainloop()
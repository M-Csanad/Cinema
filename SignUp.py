import tkinter as tk
from tkinter import *
import ttkbootstrap as ttk
from tkinter.ttk import *
from ttkbootstrap.constants import *

root = tk.Tk()
style = ttk.Style('vapor')
root.resizable(False, False)
root.eval('tk::PlaceWindow . center')
root.title('SignUp')

tk.Grid.rowconfigure(root, 0, weight=1)
tk.Grid.columnconfigure(root, 0, weight=1)

def clickEnt_vNev(args):
    vNev_inEntry.delete(0, 'end')

def clickEnt_kNev(args):
    kNev_inEntry.delete(0, 'end')

mystring = StringVar()
kNev_inEntry = Entry(root, textvariable=mystring)
kNev_inEntry.insert(0, 'Keresztnév')
kNev_inEntry.bind("<Button-1>", clickEnt_kNev)

vNev_inEntry = Entry(root, textvariable=mystring)
vNev_inEntry.insert(0, 'Keresztnév')
vNev_inEntry.bind("<Button-1>", clickEnt_vNev)

root.mainloop()
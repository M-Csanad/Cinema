import tkinter as tk
from tkinter import *
import ttkbootstrap as ttk
from tkinter.ttk import *
from ttkbootstrap.constants import *

root_sgnUp = tk.Tk()
style = ttk.Style('vapor')
root_sgnUp.resizable(False, False)
root_sgnUp.eval('tk::PlaceWindow . center')
root_sgnUp.title('SignUp')

tk.Grid.rowconfigure(root_sgnUp, 0, weight=1)
tk.Grid.columnconfigure(root_sgnUp, 0, weight=1)



row_chair = range(1, 5)
column_chair = "ABCDEF"
option = [{str(index)+itr:"0" for itr in column_chair} for index in row_chair]

button_dict={}
rowIndex = 0
columnIndex = 0
for x in option:
    for i in x:
        columnIndex += 1
        button_dict[i] = tk.Button(root_sgnUp, text=i)
        if((int(i[0])+1) != (int(i[0]))):
            print(f"ez: { int(i[0])}")
            button_dict[i].grid(row=rowIndex, column=columnIndex, sticky=NSEW)
        else:
            print(int(i[0]))
            columnIndex = 0
            rowIndex += 1
            button_dict[i].grid(row=rowIndex, column=columnIndex, sticky=NSEW)





root_sgnUp.mainloop()


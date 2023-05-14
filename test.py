import tkinter as tk
from tkinter import *
import ttkbootstrap as ttk
from tkinter.ttk import *
from ttkbootstrap.constants import *

import random

root_sgnUp = tk.Tk()
style = ttk.Style('vapor')
root_sgnUp.resizable(False, False)
root_sgnUp.eval('tk::PlaceWindow . center')
root_sgnUp.title('SignUp')

tk.Grid.rowconfigure(root_sgnUp, 0, weight=1)
tk.Grid.columnconfigure(root_sgnUp, 0, weight=1)



def clickChair(id):

    print(button_dict[id].cget('text'))



row_chair = range(1, 16)
column_chair = "ABCDEFGHIJK"
option = [{str(index)+itr:"0" for itr in column_chair} for index in row_chair]

button_dict={}

rowIndex = 0
columnIndex = 0

index = 1
for x in option:
    for i in x:
        betelt = random.randint(0, 10)
        button_dict[i] = tk.Button(root_sgnUp, text=i, command=lambda x=i:(clickChair(x)))
        if(index <= (len(column_chair))):
            button_dict[i].grid(row=rowIndex, column=columnIndex, sticky=NSEW, ipadx=5, ipady=2, pady=5, padx=5)
            if(betelt == 1):
                button_dict[i].config(background='#DC0000', disabledforeground='#FFF')
                button_dict[i]['state'] = DISABLED
        else:
            index = 1
            columnIndex = 0
            rowIndex += 1
            button_dict[i].grid(row=rowIndex, column=columnIndex, sticky=NSEW, ipadx=5, ipady=2, pady=5, padx=5)

        columnIndex += 1
        index += 1



root_sgnUp.mainloop()


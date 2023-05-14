import tkinter as tk
from tkinter import *
import ttkbootstrap as ttk
from tkinter.ttk import *
from ttkbootstrap.constants import *
import secrets





root = tk.Tk()
style = ttk.Style('vapor')
root.resizable(False, False)
root.eval('tk::PlaceWindow . center')
root.title('SignUp')

tk.Grid.rowconfigure(root, 0, weight=1)
tk.Grid.columnconfigure(root, 0, weight=1)

token = secrets.token_urlsafe(6)


def clickEnt_vNev(args):
    vNev_inEntry.delete(0, 'end')


def clickEnt_kNev(args):
    kNev_inEntry.delete(0, 'end')


kNev_inEntry = tk.Entry(root, textvariable=StringVar())
kNev_inEntry.insert(0, 'Keresztnév')
kNev_inEntry.bind("<Button-1>", clickEnt_kNev)

vNev_inEntry = tk.Entry(root, textvariable=StringVar())
vNev_inEntry.insert(0, 'Vezetéknév')
vNev_inEntry.bind("<Button-1>", clickEnt_vNev)

token_inEntry = Entry(root, textvariable=StringVar(), foreground="#fff")
token_inEntry.insert(0, f'Foglalási azonosító - {token}')
token_inEntry.configure(state=tk.DISABLED)



def Import_data():
    try:

        #help_terem()
        print(help_terem())
        kNev = kNev_inEntry.get()
        vNev = vNev_inEntry.get()
        print(kNev, vNev)
        val = [
            (token, str(kNev), str(vNev), 150, 1)
        ]

        INSERT_Foglalasok = (
            "INSERT INTO `foglalasok` VALUES (%s,%s,%s,%s,%s) ON DUPLICATE KEY UPDATE FOGLAL_SORSZAM = VALUES(FOGLAL_SORSZAM)"
        )
        cursor.executemany(INSERT_Foglalasok, val)
        cursor.execute('COMMIT')
    except Exception as e:
        print(f"-----------------{str(e)}-----------------")


btn_Run = tk.Button(root, text="Rögzítés", command=lambda: Import_data())


kNev_inEntry.grid(row=0, column=0, sticky=NSEW,
                  ipadx=5, ipady=5, padx=10, pady=10)
vNev_inEntry.grid(row=0, column=1, sticky=NSEW,
                  ipadx=5, ipady=5, padx=10, pady=10)
token_inEntry.grid(row=1, column=0, columnspan=2, sticky=NSEW,
                   ipadx=5, ipady=5, padx=10, pady=10)
btn_Run.grid(row=2, column=0, columnspan=2, sticky=NSEW,
             ipadx=5, ipady=5, padx=10, pady=10)

root.mainloop()

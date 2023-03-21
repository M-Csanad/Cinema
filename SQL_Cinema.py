import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import sqlite3
import random


# ---------SQL---------
con = sqlite3.connect("CINEMA.db")

curTer = con.cursor()
curFog = con.cursor()

curTer.execute('''CREATE TABLE IF NOT EXISTS Termek (
    Terem_szam INTEGER PRIMARY KEY,
    Terem_film TEXT,
    LOW_PRIO VARCHAR,
    Terem_maxhely INTEGER
    )''')

curFog.execute('''CREATE TABLE IF NOT EXISTS Foglalások (
    Foglal_sorszam INTEGER PRIMARY KEY,
    Keresztnev TEXT,
    Vezetéknev TEXT,
    Szekszam INTEGER,
    
    Teremszam INTEGER,
    FOREIGN KEY (Teremszam) REFERENCES Termek(Terem_szam)
    )''')


curTer.execute("""INSERT OR REPLACE INTO Termek VALUES
        (01, 'Film01', '2020;Horror;120perc', 250),
        (02, 'Film02', '2020;Comedy;140perc', 250),
        (03, 'Film03', '2020;Fantasy;90perc', 150),
        (04, 'Film04', '2021;Thriller;110perc', 250)
        """)

def Foglal():
    None

def Info(terem, film, lwp, maxh):

    root_info = tk.Tk()
    style_info = ttk.Style('darkly')
    root_info.resizable(False, False)
    root_info.eval('tk::PlaceWindow . center')
    root_info.title('Jegyfoglalás')
    
    betelt = random.randint(0, maxh)
    date = lwp[0]
    category = lwp[1]
    time = lwp[2]

    teremszam_lb = ttk.Label(root_info, text=f"Teremszám: {terem}", background='#222222', foreground='#F8F9FA')
    film_lb = ttk.Label(root_info, text=f"Vetített film: {film}", background='#222222', foreground='#F8F9FA')
    low_prio_lb = ttk.Label(root_info, text=f"Egyéb információ: \n\tÉv: {date}\n\tKategória: {category}\n\tJátékidő: {time}", background='#222222', foreground='#F8F9FA')
    maxhely_lb = ttk.Label(root_info, text=f"Összes ülőhelyek száma: {maxh}", background='#222222', foreground='#F8F9FA')
    szabad_lb = ttk.Label(root_info, text=f"Szabad ülőhelyek száma: {maxh-betelt}", background='#222222', foreground='#F8F9FA')

    btn = ttk.Button(root_info, text="Jegyfoglalás", bootstyle=DARK ,command=lambda:Foglal)

    
    teremszam_lb.grid(row=0, column=0, sticky=W, padx=5, pady=5)
    film_lb.grid(row=1, column=0, sticky=W, padx=5, pady=5)
    low_prio_lb.grid(row=2, column=0, sticky=W, padx=5, pady=5)
    maxhely_lb.grid(row=3, column=0, sticky=W, padx=5, pady=5)
    szabad_lb.grid(row=4, column=0, sticky=W, padx=5, pady=5)
    
    btn.grid(row=2, column=1, sticky=E, padx=5, pady=5)


# ---------/SQL---------

root = tk.Tk()
style = ttk.Style('darkly')
root.resizable(False, False)
root.eval('tk::PlaceWindow . center')
root.title('Cinema')

tk.Grid.rowconfigure(root, 0, weight=1)
tk.Grid.columnconfigure(root, 0, weight=1)


select = curTer.execute(
    "SELECT Terem_szam, Terem_film, LOW_PRIO, Terem_maxhely FROM Termek")


teremszam_lst = []
film_lst = []
low_prio_lst = []
maxhely_lst = []

for data in (select):
    teremszam_lst.append(data[0])
    film_lst.append(data[1])
    low_prio_lst.append(data[2])
    maxhely_lst.append(data[3])

lwp_lst = []
for index in low_prio_lst:
    lwp_lst.append(index.split(';'))


btn01 = ttk.Button(root, text=film_lst[0], bootstyle=DARK, command=lambda: Info(
    teremszam_lst[0], film_lst[0], lwp_lst[0], maxhely_lst[0]))
btn02 = ttk.Button(root, text=film_lst[1], bootstyle=DARK, command=lambda: Info(
    teremszam_lst[1], film_lst[1], lwp_lst[1], maxhely_lst[1]))
btn03 = ttk.Button(root, text=film_lst[2], bootstyle=DARK, command=lambda: Info(
    teremszam_lst[2], film_lst[2], lwp_lst[2], maxhely_lst[2]))
btn04 = ttk.Button(root, text=film_lst[3], bootstyle=DARK, command=lambda: Info(
    teremszam_lst[3], film_lst[3], lwp_lst[3], maxhely_lst[3]))


# curTer.execute("""INSERT INTO Foglalások VALUES
#        (00001, 'KeresztN01', 'VezetekN01', 001, 001),
#        (00002, 'KeresztN02', 'VezetekN02', 125, 002),
#        (00003, 'KeresztN03', 'VezetekN03', 111, 003),
#        (00004, 'KeresztN04', 'VezetekN04', 92, 004),
#        (00005, 'KeresztN05', 'VezetekN05', 101, 005),
#        (00006, 'KeresztN06', 'VezetekN06', 077, 006),
#        (00007, 'KeresztN07', 'VezetekN07', 002, 001),
#        """)


btn01.grid(row=0, column=0, sticky=NSEW, ipadx=20, ipady=20, padx=5, pady=5)
btn02.grid(row=0, column=1, sticky=NSEW, ipadx=20, ipady=20, padx=5, pady=5)
btn03.grid(row=1, column=0, sticky=NSEW, ipadx=20, ipady=20, padx=5, pady=5)
btn04.grid(row=1, column=1, sticky=NSEW, ipadx=20, ipady=20, padx=5, pady=5)


con.commit()
con.close()
root.mainloop()

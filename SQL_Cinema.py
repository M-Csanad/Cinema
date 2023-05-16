import tkinter as tk
from tkinter import *
from tkinter import messagebox
import ttkbootstrap as ttk
from tkinter.ttk import *
from ttkbootstrap.constants import *
import random
import secrets
import os
from PIL import Image, ImageTk
import TestConnection
import CreateDatabase
from CreateDatabase import *

exec(open('TestConnection.py').read())
exec(open('CreateDatabase.py').read())

# Szebb verzió, ha az exec nem működik:
# import os
# os.system('py CreateDatabase.py')
# os.system('py TestConnection.py')

cursor = CreateDatabase.cursor



#==========================#
#   SignUp - Chair generator
#==========================#

def Call_SignUp(terem, ticket_2D, ticket_3D, ticket_2D_db, ticket_3D_db):
    global betelt, maxhely
    print(betelt, maxhely)

    root_sgnUp = tk.Tk()
    style = ttk.Style('vapor')
    root_sgnUp.resizable(False, False)
    root_sgnUp.eval('tk::PlaceWindow . center')
    root_sgnUp.title('SignUp')

    tk.Grid.rowconfigure(root_sgnUp, 0, weight=1)
    tk.Grid.columnconfigure(root_sgnUp, 0, weight=1)
    frame_RG = tk.Frame(root_sgnUp)
    frame_LF = tk.Frame(root_sgnUp)

    global ticket_chairCount
    def clickResetColor(id):
        global ticket_chairCount
        ticket_chairCount -= 1
        button_dict[id].config(background='#03C988', foreground='#F8F9FA', command=lambda: (clickColor(id)))
    def clickColor(id):
        global ticket_chairCount
        if ((ticket_chairCount >= ticket_2D_db) and (ticket_2D != "NONE")):
            tk.messagebox.showerror(title="Error", message="Több széket nem jelölhet, mint amennyi jegyet kért")
        if((ticket_chairCount >= ticket_3D_db) and (ticket_3D != "NONE")):
            tk.messagebox.showerror(title="Error", message="Több széket nem jelölhet, mint amennyi jegyet kért")

        if ((ticket_chairCount <= ticket_2D_db-1) and (ticket_2D != "NONE")):
            button_dict[id].config(background='#F7C04A', foreground='#000', command=lambda:(clickResetColor(id)))
            ticket_chairCount += 1
            print(ticket_chairCount)
        if ((ticket_chairCount <= ticket_3D_db-1) and (ticket_3D != "NONE")):
            button_dict[id].config(background='#F7C04A', foreground='#000', command=lambda:(clickResetColor(id)))
            ticket_chairCount += 1

#==========================#
#   SignUp - THE Generator
#==========================#

    if (maxhely == 150):
        row_chair = range(1, 16)
        column_chair = "ABCDEFGHIJ"
    if (maxhely == 120):
        row_chair = range(1, 16)
        column_chair = "ABCDEFGH"
    if (maxhely == 100):
        row_chair = range(1, 6)
        column_chair = "ABCDEFGHIJKLMNOPQRST"

    option = [{str(index)+itr: "0" for itr in column_chair}
              for index in row_chair]

    button_dict = {}
    rowIndex = 0
    columnIndex = 0
    ticket_chairCount = 0
    index = 1
    for x in option:
        for i in x:
            button_dict[i] = tk.Button(
                frame_RG, text=i, command=lambda x=i: (clickColor(x)))
            button_dict[i].config(background='#03C988', foreground='#F8F9FA')
            if (index <= (len(column_chair))):
                button_dict[i].grid(row=rowIndex, column=columnIndex,
                                    sticky=NSEW, ipadx=5, ipady=2, pady=5, padx=5)
            else:
                index = 1
                columnIndex = 0
                rowIndex += 1
                button_dict[i].grid(row=rowIndex, column=columnIndex,
                                    sticky=NSEW, ipadx=5, ipady=2, pady=5, padx=5)
            columnIndex += 1
            index += 1

    betelt_count = 0
    index = 0
    while ((betelt-1 >= betelt_count)):
        print(f"Betelt: {betelt}\nSzámláló: {betelt_count}")
        for i in button_dict:
            rand = random.randint(1,3)
            if((betelt-1 >= betelt_count) and (rand == 2)):
                if(button_dict[i]['state'] != DISABLED):
                    button_dict[i].config(background='#DC0000', disabledforeground='#FFF')
                    button_dict[i]['state'] = DISABLED
                    betelt_count += 1
                else:
                    betelt_count = betelt_count
            index += 1
            if (index == len(button_dict)-1):
                print("\nbetelt_szamlalo: " + str(betelt_count))
                print("i: " + str(index))
                index = 0
        betelt_count = betelt_count



#==========================#
#   SignUp - User Info
#==========================#

    token = secrets.token_urlsafe(6)

    def clickEnt_vNev(args):
        vNev_inEntry.delete(0, 'end')

    def clickEnt_kNev(args):
        kNev_inEntry.delete(0, 'end')

    kNev_inEntry = tk.Entry(frame_LF, textvariable=StringVar())
    kNev_inEntry.insert(0, 'Keresztnév')
    kNev_inEntry.bind("<Button-1>", clickEnt_kNev)

    vNev_inEntry = tk.Entry(frame_LF, textvariable=StringVar())
    vNev_inEntry.insert(0, 'Vezetéknév')
    vNev_inEntry.bind("<Button-1>", clickEnt_vNev)

    token_inEntry = tk.Entry(
        frame_LF, textvariable=StringVar(), foreground="#fff")
    token_inEntry.insert(0, f'Foglalási azonosító - {token}')
    token_inEntry.configure(state=tk.DISABLED)



#==========================#
#   SignUp - Import SQL
#==========================#

    def Import_data():
        try:
            ticket_chair = []
            for i in button_dict:
                if(button_dict[i].cget('bg') == "#F7C04A"):
                    ticket_chair.append(button_dict[i].cget('text'))
            print(len(ticket_chair), ticket_2D_db)
            if (len(ticket_chair) < ticket_2D_db):
                tk.messagebox.showinfo(title="", message="Kevesebb széket jelölt be, mint ahány jegyet kért")
            if (len(ticket_chair) == ticket_2D_db):
                kNev = kNev_inEntry.get()
                vNev = vNev_inEntry.get()
                val = [
                    (token, str(kNev), str(vNev), str(ticket_chair), terem)
                ]

                INSERT_Foglalasok = (
                    "INSERT INTO `foglalasok` VALUES (%s,%s,%s,%s,%s) ON DUPLICATE KEY UPDATE FOGLAL_SORSZAM = VALUES(FOGLAL_SORSZAM)"
                )
                cursor.executemany(INSERT_Foglalasok, val)
                cursor.execute('COMMIT')
                root_sgnUp.destroy()
        except Exception as e:
            print(f"-----------------{str(e)}-----------------")

    btn_Run = tk.Button(frame_LF, text="Rögzítés", command=lambda: (
        Import_data()))

    frame_RG.grid(row=0, column=1, sticky=EW)
    frame_LF.grid(row=0, column=0, sticky=EW)

    frame_LF.grid_rowconfigure(0, weight=1)

    kNev_inEntry.grid(row=0, column=0, sticky=NSEW,
                      ipadx=5, ipady=5, padx=10, pady=10)
    vNev_inEntry.grid(row=0, column=1, sticky=NSEW,
                      ipadx=5, ipady=5, padx=10, pady=10)
    token_inEntry.grid(row=1, column=0, columnspan=2, sticky=NSEW,
                       ipadx=5, ipady=5, padx=10, pady=10)
    btn_Run.grid(row=2, column=0, columnspan=2, sticky=NSEW,
                 ipadx=5, ipady=5, padx=10, pady=10)

    kNev_inEntry.grid_rowconfigure(1, weight=1)
    vNev_inEntry.grid_rowconfigure(1, weight=1)
    token_inEntry.grid_rowconfigure(1, weight=1)
    btn_Run.grid_rowconfigure(1, weight=1)

    root_sgnUp.mainloop()



#==========================#
#   Ticket - Error Check
#==========================#

def TicketCheck(price, ticket_2D, ticket_3D, ticket_2D_db, ticket_3D_db, terem):
    price = int(price)
    ticket_2D_db = int(ticket_2D_db)
    ticket_3D_db = int(ticket_3D_db)

    full_price = ((price*ticket_2D_db) + ((price+730)*ticket_3D_db))

    ticket_countErrorCheck = 0

    if ((ticket_2D != ('NONE')) and (ticket_2D_db == 0)) or ((ticket_3D != ('NONE')) and (ticket_3D_db == 0)):
        print("Helytelen - no count")
    else:
        ticket_countErrorCheck += 1

    if ((ticket_2D == ('NONE')) and (ticket_2D_db != 0)) or ((ticket_3D == ('NONE')) and (ticket_3D_db != 0)):
        print("Helytelen - no ticket type")
    else:
        ticket_countErrorCheck += 1

    if (ticket_2D == ('NONE')) and (ticket_3D == ('NONE')):
        print("Valamit kell választani")

    else:
        ticket_countErrorCheck += 1

    if ticket_countErrorCheck == 3:

        Call_SignUp(terem, ticket_2D, ticket_3D, ticket_2D_db, ticket_3D_db)



#==========================#
#   Booking - Graphics
#==========================#

def Foglal(price, terem):

    root_foglal = tk.Tk()
    style = ttk.Style('vapor')
    root_foglal.resizable(False, False)
    root_foglal.eval('tk::PlaceWindow . center')
    root_foglal.title('Cinema')

    tk.Grid.rowconfigure(root, 0, weight=1)
    tk.Grid.columnconfigure(root, 0, weight=1)

    lb_title = tk.Label(root_foglal, text="JEGYEK KIVÁLASZTÁSA",
                        justify=CENTER, anchor=CENTER)
    lb_text00 = tk.Label(root_foglal, text="IDŐPONT",
                         justify=CENTER, anchor=CENTER)
    lb_text01 = tk.Label(root_foglal, text="TÍPUS",
                         justify=CENTER, anchor=CENTER)
    lb_text02 = tk.Label(root_foglal, text="ÁR/DB",
                         justify=CENTER, anchor=CENTER)
    lb_text03 = tk.Label(root_foglal, text="DARAB",
                         justify=CENTER, anchor=CENTER)
    lb_text04 = tk.Label(root_foglal, text="JEGY KATEGÓRIA",
                         justify=CENTER, anchor=CENTER)
    lb_time3D = tk.Label(root_foglal, text="14:05",
                         justify=CENTER, anchor=CENTER)
    lb_time2D = tk.Label(root_foglal, text="18:00",
                         justify=CENTER, anchor=CENTER)

    lb_3D = tk.Label(root_foglal, text="3D", justify=CENTER, anchor=CENTER)
    lb_2D = tk.Label(root_foglal, text="2D", justify=CENTER, anchor=CENTER)
    lb_price2D = tk.Label(
        root_foglal, text=f"{price}", justify=CENTER, anchor=CENTER)
    lb_price3D = tk.Label(
        root_foglal, text=f"{(int(price)+730)}", justify=CENTER, anchor=CENTER)

    menu3D_C = tk.StringVar(root_foglal)
    menu3D_C.set("NONE")
    drop3D_C = tk.OptionMenu(root_foglal, menu3D_C, "NONE",
                             "Junior", "Senior", "Felnőtt", "Kedvezményezett")
    drop3D_C.config(bg="#1A0933", fg="#32FBE2",
                    activebackground="#30125F", activeforeground="#32FBE2")
    drop3D_C["menu"].config(bg="#1A0933", fg="#32FBE2",
                            activebackground="#30125F", activeforeground="#32FBE2")

    menu2D_C = tk.StringVar(root_foglal)
    menu2D_C.set("NONE")
    drop2D_C = tk.OptionMenu(root_foglal, menu2D_C, "NONE",
                             "Junior", "Senior", "Felnőtt", "Kedvezményezett")
    drop2D_C.config(bg="#1A0933", fg="#32FBE2",
                    activebackground="#30125F", activeforeground="#32FBE2")
    drop2D_C["menu"].config(bg="#1A0933", fg="#32FBE2",
                            activebackground="#30125F", activeforeground="#32FBE2")

    menu2D_DB = tk.StringVar(root_foglal)
    menu2D_DB.set("0")
    drop2D_DB = tk.OptionMenu(
        root_foglal, menu2D_DB, "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10")
    drop2D_DB.config(bg="#1A0933", fg="#32FBE2",
                     activebackground="#30125F", activeforeground="#32FBE2")
    drop2D_DB["menu"].config(bg="#1A0933", fg="#32FBE2",
                             activebackground="#30125F", activeforeground="#32FBE2")

    menu3D_DB = tk.StringVar(root_foglal)
    menu3D_DB.set("0")
    drop3D_DB = tk.OptionMenu(
        root_foglal, menu3D_DB, "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10")
    drop3D_DB.config(bg="#1A0933", fg="#32FBE2",
                     activebackground="#30125F", activeforeground="#32FBE2")
    drop3D_DB["menu"].config(bg="#1A0933", fg="#32FBE2",
                             activebackground="#30125F", activeforeground="#32FBE2")

    done_ticket = tk.Button(root_foglal, text="JEGY LEFOGLALÁSA", anchor=CENTER, command=lambda: TicketCheck(
        price, (menu2D_C.get()), (menu3D_C.get()), (menu2D_DB.get()), (menu3D_DB.get()), terem))


    lb_title.grid(row=0, column=0, columnspan=6, sticky=EW,
                  ipadx=5, ipady=5, padx=10, pady=(10, 25))
    lb_text00.grid(row=1, column=0, sticky=NSEW, ipadx=5,
                   ipady=5, padx=10, pady=(5, 25))
    lb_text01.grid(row=1, column=2, sticky=NSEW, ipadx=5,
                   ipady=5, padx=10, pady=(5, 25))
    lb_text02.grid(row=1, column=3, sticky=NSEW, ipadx=5,
                   ipady=5, padx=10, pady=(5, 25))
    lb_text03.grid(row=1, column=4, sticky=NSEW, ipadx=5,
                   ipady=5, padx=10, pady=(5, 25))
    lb_text04.grid(row=1, column=5, sticky=NSEW, ipadx=5,
                   ipady=5, padx=10, pady=(5, 25))

    lb_time3D.grid(row=2, column=0, sticky=NSEW,
                   ipadx=5, ipady=5, padx=10, pady=10)
    lb_time2D.grid(row=3, column=0, sticky=NSEW,
                   ipadx=5, ipady=5, padx=10, pady=10)
    lb_3D.grid(row=2, column=2, sticky=NSEW,
               ipadx=5, ipady=5, padx=10, pady=10)
    lb_2D.grid(row=3, column=2, sticky=NSEW,
               ipadx=5, ipady=5, padx=10, pady=10)
    lb_price3D.grid(row=2, column=3, sticky=NSEW,
                    ipadx=5, ipady=5, padx=10, pady=10)
    lb_price2D.grid(row=3, column=3, sticky=NSEW,
                    ipadx=5, ipady=5, padx=10, pady=10)
    drop3D_C.grid(row=2, column=5, sticky=NSEW,
                  ipadx=5, ipady=5, padx=10, pady=10)
    drop2D_C.grid(row=3, column=5, sticky=NSEW,
                  ipadx=5, ipady=5, padx=10, pady=10)
    drop3D_DB.grid(row=2, column=4, sticky=NSEW,
                   ipadx=5, ipady=5, padx=10, pady=10)
    drop2D_DB.grid(row=3, column=4, sticky=NSEW,
                   ipadx=5, ipady=5, padx=10, pady=10)
    done_ticket.grid(row=4, column=0, columnspan=6, sticky=NSEW,
                     ipadx=5, ipady=5, padx=10, pady=10)

    root_foglal.mainloop()



#==========================#
#   Movie Info - Info
#==========================#

def Info(terem, film, maxh, lp_ye, lp_ca, lp_pl, price, lp_id, lp_age):
    global betelt, maxhely
    terem = int(terem)
    maxh = int(maxh)
    lp_ye = int(lp_ye)
    lp_pl = int(lp_pl)
    maxhely = maxh

    root_info = Toplevel()  # a framebe beágyazott kép Toplevel segítségével jelenik csak meg
    style_info = ttk.Style('vapor')
    root_info.resizable(False, False)
    root_info.title('FilmInfo')
    imgFrame = tk.Frame(root_info)

    betelt = random.randint(0, maxh)
    date = lp_ye
    category = lp_ca
    time = lp_pl
    age = lp_age

    with open('txt/filminfok.txt', 'r', encoding='utf-8') as f:
        lines = [line.strip('\n') for line in f]

    kep = Image.open(f"képek/0{lp_id}.png")
    width, height = kep.size
    weightSM = (int(width/1.2))
    heightSm = (int(height/1.2))
    kepSize = kep.resize((weightSM, heightSm))
    ujkep = ImageTk.PhotoImage(kepSize)
    kep1 = tk.Label(imgFrame, image=ujkep)

    film_lb = tk.Label(
        root_info, text=f"{film}", background='#1A0933', foreground='#F8F9FA')
    film_date = tk.Label(
        root_info, text=f"{date}", background='#1A0933', foreground='#F8F9FA')
    film_desc_TXT = tk.Text(
        root_info, background='#1A0933', foreground='#F8F9FA')
    film_desc_TXT.insert(INSERT, f"{lines[lp_id]}")

    lb_TXT = film_desc_TXT.get("1.0", END)
    film_desc = Label(root_info, text=lb_TXT, background='#1A0933',
                      foreground='#F8F9FA', wraplength=330)

    film_age = tk.Label(
        root_info, text=f"{age}", background='#1A0933', foreground='#F8F9FA')

    low_prio_lb = tk.Label(
        root_info, text=f"{category} | {time}perc", background='#1A0933', foreground='#F8F9FA')

    maxhely_lb = tk.Label(
        root_info, text=f"Összes ülőhelyek száma: {maxh}", background='#1A0933', foreground='#F8F9FA')
    szabad_lb = tk.Label(
        root_info, text=f"Szabad ülőhelyek száma: {maxh}/{maxh-betelt}", background='#1A0933', foreground='#F8F9FA')
    teremszam_lb = tk.Label(
        root_info, text=f"Teremszám: {terem}", background='#1A0933', foreground='#F8F9FA')

    btn = tk.Button(root_info, text="Jegyfoglalás",
                    bg='#1A0933', command=lambda: Foglal(price, terem))

    kep1.pack()
    imgFrame.grid(row=0, column=5, rowspan=5, sticky=NSEW)

    film_lb.grid(row=0, column=0, sticky=W, padx=5, pady=5)
    film_date.grid(row=0, column=1, sticky=W, padx=5, pady=5)
    film_desc.grid(row=1, column=0, columnspan=2, sticky=W, padx=5, pady=5)
    low_prio_lb.grid(row=2, column=0, sticky=W, padx=5, pady=5)
    film_age.grid(row=2, column=1, sticky=W, padx=5, pady=5)
    szabad_lb.grid(row=3, column=1, sticky=W, padx=5, pady=5)
    # maxhely_lb.grid(row=2, column=0, sticky=W, padx=5, pady=5)
    # szabad_lb.grid(row=3, column=0, sticky=W, padx=5, pady=5)
    # teremszam_lb.grid(row=4, column=0, sticky=W, padx=5, pady=5)

    btn.grid(row=3, column=0, sticky=EW, padx=5, pady=5, ipadx=10, ipady=10)

    root_info.mainloop()



#==========================#
#   Basic Menu - Start Panel
#==========================#

root = tk.Tk()
style = ttk.Style('vapor')
root.resizable(False, False)
root.eval('tk::PlaceWindow . center')
root.title('Cinema')

tk.Grid.rowconfigure(root, 0, weight=1)
tk.Grid.columnconfigure(root, 0, weight=1)


select = cursor.execute(
    "SELECT termek.TEREM_SZAM, termek.TEREM_FILM, termek.TEREM_MAXHELY, low_prio.YEAR, low_prio.CATEGORY, low_prio.PLAYTIME, low_prio.PRICE, low_prio.LP_ID, low_prio.AGE FROM termek INNER JOIN low_prio ON termek.LOW_PRIO = low_prio.LP_ID")

teremszam_lst = []
film_lst = []
maxhely_lst = []
LP_year_lst = []
LP_category_lst = []
LP_playtime_lst = []
LP_price_lst = []
LP_age_lst = []
LP_ID = []

for data in (cursor.fetchall()):
    teremszam_lst.append(data[0])
    film_lst.append(data[1])
    maxhely_lst.append(data[2])
    LP_year_lst.append(data[3])
    LP_category_lst.append(data[4])
    LP_playtime_lst.append(data[5])
    LP_price_lst.append(data[6])
    LP_ID.append(data[7])
    LP_age_lst.append(data[8])


btn01 = Button(root, text=film_lst[0], style=LIGHT, command=lambda: Info(
    teremszam_lst[0], film_lst[0], maxhely_lst[0], LP_year_lst[0], LP_category_lst[0], LP_playtime_lst[0], LP_price_lst[0], LP_ID[0], LP_age_lst[0]))

btn02 = Button(root, text=film_lst[1], style=LIGHT, command=lambda: Info(
    teremszam_lst[1], film_lst[1], maxhely_lst[1], LP_year_lst[1], LP_category_lst[1], LP_playtime_lst[1], LP_price_lst[1], LP_ID[1], LP_age_lst[1]))

btn03 = Button(root, text=film_lst[2], style=LIGHT, command=lambda: Info(
    teremszam_lst[2], film_lst[2], maxhely_lst[2], LP_year_lst[2], LP_category_lst[2], LP_playtime_lst[2], LP_price_lst[2], LP_ID[2], LP_age_lst[2]))

btn04 = Button(root, text=film_lst[3], style=LIGHT, command=lambda: Info(
    teremszam_lst[3], film_lst[3], maxhely_lst[3], LP_year_lst[3], LP_category_lst[3], LP_playtime_lst[3], LP_price_lst[3], LP_ID[3], LP_age_lst[3]))

btn05 = Button(root, text=film_lst[4], style=LIGHT, command=lambda: Info(
    teremszam_lst[4], film_lst[4], maxhely_lst[4], LP_year_lst[4], LP_category_lst[4], LP_playtime_lst[4], LP_price_lst[4], LP_ID[4], LP_age_lst[4]))

btn06 = Button(root, text=film_lst[5], style=LIGHT, command=lambda: Info(
    teremszam_lst[5], film_lst[5], maxhely_lst[5], LP_year_lst[5], LP_category_lst[5], LP_playtime_lst[5], LP_price_lst[5], LP_ID[5], LP_age_lst[5]))


btn01.grid(row=0, column=0, sticky=NSEW, ipadx=20, ipady=25, padx=10, pady=10)
btn02.grid(row=0, column=1, sticky=NSEW, ipadx=20, ipady=25, padx=10, pady=10)
btn03.grid(row=0, column=2, sticky=NSEW, ipadx=20, ipady=25, padx=10, pady=10)
btn04.grid(row=1, column=0, sticky=NSEW, ipadx=20, ipady=25, padx=10, pady=10)
btn05.grid(row=1, column=1, sticky=NSEW, ipadx=20, ipady=25, padx=10, pady=10)
btn06.grid(row=1, column=2, sticky=NSEW, ipadx=20, ipady=25, padx=10, pady=10)


root.mainloop()

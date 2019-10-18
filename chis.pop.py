from random import *
from tkinter import *

#первое

mainloop = Tk()
mainloop.title("Численность популяций")
mainloop.geometry("350x500")
mainloop.resizable(False, False)


neogrost=Label(mainloop, text = 'Неограниченный рост')
neogrost.place ( x = 100, y = 10)

A=Label(mainloop, text = 'A')
A.place (x = 10, y = 40)

zher1=Entry(mainloop, width = 5)
zher1.place(x = 25, y = 40)

bt_neogrost = Button (mainloop, text = 'Неограниченный рост', bg = "gray")
bt_neogrost.place(x = 65, y = 34)

entr1 = Label(mainloop, text = "Тут появится значение" )
entr1.place(x=210, y=40)

# второе

ogrrost=Label(mainloop, text = 'Ограниченный рост')
ogrrost.place(x=105, y=70)

B=Label(mainloop, text = 'B')
B.place (x=10, y=100)

zher2=Entry(mainloop, width = 5)
zher2.place(x = 25, y = 100)

bt_ogrrost = Button (mainloop, text = 'Ограниченный рост', bg = "gray")
bt_ogrrost.place(x = 65, y = 94)

entr2 = Label(mainloop, text = "Тут появится значение" )
entr2.place(x=198, y=100)

# третье

otlov=Label(mainloop, text = 'Ограниченный рост с отловом')
otlov.place(x=70, y=130)

С=Label(mainloop, text = 'С')
С.place (x=10, y=160)

zher3=Entry(mainloop, width = 5)
zher3.place(x = 25, y = 160)

otlov = Button (mainloop, text = 'Ограниченный рост с отловом', bg = "gray")
otlov.place(x = 65, y = 154)

entr3 = Label(mainloop, text = "Тут" )
entr3.place(x=255, y=160)

# четвертое

hish=Label(mainloop, text = 'Жертва-хищник')
hish.place(x=115, y=190)

D=Label(mainloop, text = 'D')
D.place (x=10, y=220)

zher4=Entry(mainloop, width = 5)
zher4.place(x = 25, y = 220)

bt_hish = Button (mainloop, text = 'Жертва-хищник', bg = "gray")
bt_hish.place(x = 170, y = 214)

F=Label(mainloop, text = 'F')
F.place (x=60, y=220)

zher5=Entry(mainloop, width = 5)
zher5.place(x = 75, y = 220)

G=Label(mainloop, text = "G")
G.place(x=110, y=220)

zher6=Entry(mainloop, width = 5)
zher6.place(x = 125, y = 220)

zhertvi=Label(mainloop, text='Жертвы')
zhertvi.place(x=40, y=245)

zhertvi2=Label(mainloop, text = 'Рез.')
zhertvi2.place(x=90, y = 245)

hishnik=Label(mainloop, text='Хищники')
hishnik.place(x=140, y=245)

hishnik1=Label(mainloop, text = 'Рез.')
hishnik1.place(x=200, y=245)

# рядом с канвасом

zhertvican=Label(mainloop, text='Жертвы')
zhertvican.place(x=10, y=285)

zher7=Entry(mainloop, width = 5)
zher7.place(x = 85, y = 285)

hishcan=Label(mainloop, text='Хищники')
hishcan.place(x=10, y=315)

zher8=Entry(mainloop, width = 5)
zher8.place(x = 85, y = 315)

cikl=Label(mainloop, text='Кол. циклов')
cikl.place(x=10, y=345)

kolcikl=Entry(mainloop, width = 5)
kolcikl.place(x = 85, y = 345)

bt_grafik=Button(mainloop, text='График', bg="Gray")
bt_grafik.place(x=40, y = 415)

canv=Canvas(mainloop, width=200, heigh=200, bg='gray', )
canv.place(x=130, y=280)

# привязка к кнопкам

def neogr_rost(event):
    a = float(zher1.get())
    N = int(kolcikl.get()) 
    gertv = int(zher7.get())
    for i in range(N):
        gertv = gertv*a
    entr1["text"] = str(int(gertv))
bt_neogrost.bind("<Button-1>",neogr_rost)

def ogr(event):
    a=float(zher1.get())
    b=float(zher2.get())
    N=int(kolcikl.get())
    jertv=int(zher7.get())
    for i in range(N):
        jertv=jertv*(a-b*jertv)
    entr2["text"]=str(int(jertv))
bt_ogrrost.bind("<Button-1>", ogr)

def ogr_s_otl(event):
    a=float(zher1.get())
    b=float(zher2.get())
    c=float(zher3.get())
    N=int(kolcikl.get())
    jertv=int(zher7.get())
    for i in range(N):
        jertv=(a-b*jertv)*jertv-c
    entr3["text"]=str(int(jertv))
otlov.bind("<Button-1>", ogr_s_otl)

def jer_xi(event):
    a=float(zher1.get())
    b=float(zher2.get())
    c=float(zher3.get())
    d=float(zher4.get())
    f=float(zher5.get())
    g=float(zher6.get())
    N=int(kolcikl.get())
    jertv=int(zher7.get())
    xi=int(zher8.get())
    for i in range(N):
        jertv=(a-b*jertv)*jertv-c-f*jertv*xi
        xi=d*xi+g*jertv*xi
    zhertvi2 ["text"]=str(int(jertv))
    hishnik1["text"]=str(int(xi))
bt_hish.bind("<Button-1>", jer_xi)









    

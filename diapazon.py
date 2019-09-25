import tkinter
from tkinter import *
from math import *
root=Tk()
root.title('Диапазон углов')
root.geometry("350x150")
labelV0=Label(root, text='Vo')
labelV0.place(x=10, y=10)
labelS=Label(root, text='S')
labelS.place(x=10, y=40)
labelH=Label(root, text='H')
labelH.place(x=10, y=70)
labela=Label(root, text='A')
labela.place(x=10, y=110)
labelgr1=Label(root, width=14)
labelgr1.place(x=40, y=115)
etrv0=Entry(root, width=7)
etrv0.place(x=30, y=10)
etrs=Entry(root, width=7)
etrs.place(x=30, y=40)
etrh=Entry(root, width=7)
etrh.place(x=30, y=70)
etrgr=Entry(root, width=25)
etrgr.place(x=40, y=110)
labelotvet=Label(root, text='Градусов')
labelotvet.place(x=200, y=110)
labelms=Label(root, text='м/с')
labelms.place(x=90, y=10)
labelm1=Label(root, text='м')
labelm1.place(x=90, y=40)
labelm2=Label(root, text='м')
labelm2.place(x=90, y=70)
bt=Button(root, text='Диапазон углов')
bt.place(x=120, y=37)

def f_calc(event):
    s = ''
    v_0 = int(labelV0.get())
    g = 9.8
    s = int(labelS.get())
    h = int(labelH.get())
    for a in range(1,90):
        if 0<=s*tan(radians(a)) - (g*(s**2))/(2*v_0**2*cos(radians(a))**2) <=h:
            labelgr1['text']+=str(a)+' '

    #bt['command'] = s*tan(radians(a)) - (g*(s**2))/(2*v_0**2*cos(radians(a))**2)
    #if bt>0:
        #etrgr['text'] = bt
    etrgr = s*tan(radians(a)) - (g*(s**2))/(2*v_0**2*cos(radians(a))**2)
    if etrgr>0:
        etrgr['text'] 
        

root.mainloop()

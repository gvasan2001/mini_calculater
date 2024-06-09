import tkinter as tk


window=tk.Tk()
a=tk.IntVar()
b=tk.IntVar()

window.geometry("500x500")

def add():
    aa=a.get()
    bb=b.get()
    c=aa+bb
    lab=tk.Label(window,text=c)
    lab.grid(row=4,column=0)


entry=tk.Entry(window, textvariable=a)
entry.grid(row=0,column=0)
entry1=tk.Entry(window, textvariable=b)
entry1.grid(row=1,column=0)

butten_f=tk.Frame(window, width=200,height=400)
butten_f.grid(row=3,column=0)
butten=tk.Button(butten_f,text="+" ,command=add)
butten.grid(row=3,column=0)
butten=tk.Button(butten_f,text="-")
butten.grid(row=3,column=1)
butten=tk.Button(butten_f,text="*")
butten.grid(row=3,column=2)
butten=tk.Button(butten_f,text="%")
butten.grid(row=3,column=3)
window.mainloop()
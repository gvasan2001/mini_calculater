from tkinter import *

# Initialize the root window
root = Tk()
root.title("Sci-Calculator")

def add_number(number):
    entry.insert(0,number)
# Create and pack the top frame
entry=Entry(root)
entry.grid(row=0,column=0,columnspan=7,rowspan=2)

#creat Button
button_red=Button(root, text="red",padx=10,pady=10,command=lambda:add_number(7))
button_inv=Button(root, text="inv",padx=10,pady=10,command=lambda:add_number(7))
button_pi=Button(root, text="pi",padx=10,pady=10,command=lambda:add_number(7))
button_e=Button(root, text="e",padx=10,pady=10,command=lambda:add_number(7))
button_Ans=Button(root, text="Ans",padx=10,pady=10,command=lambda:add_number(7))

button_Deg=Button(root, text="Deg",padx=10,pady=10,command=lambda:add_number(7))
button_Sin=Button(root, text="Sin",padx=10,pady=10,command=lambda:add_number(7))
button_Cos=Button(root, text="Cos",padx=10,pady=10,command=lambda:add_number(7))
button_tan=Button(root, text="tan",padx=10,pady=10,command=lambda:add_number(7))
button_Exp=Button(root, text="Exp",padx=10,pady=10,command=lambda:add_number(7))

button_X=Button(root, text="X!",padx=10,pady=10,command=lambda:add_number(7))
button_in=Button(root, text="in",padx=10,pady=10,command=lambda:add_number(7))
button_Log=Button(root, text="Log",padx=10,pady=10,command=lambda:add_number(7))
button_root=Button(root, text="root",padx=10,pady=10,command=lambda:add_number(7))
button_xY=Button(root, text="xy",padx=10,pady=10,command=lambda:add_number(7))

button_open=Button(root, text="(",padx=10,pady=10,command=lambda:add_number(7))
button_7=Button(root, text="7",padx=10,pady=10,command=lambda:add_number(7))
button_4=Button(root, text="4",padx=10,pady=10,command=lambda:add_number(4))
button_1=Button(root, text="1",padx=10,pady=10,command=lambda:add_number(1))
button_0=Button(root, text="0",padx=10,pady=10,command=lambda:add_number(0))

button_close=Button(root, text=")",padx=10,pady=10,command=lambda:add_number(7))
button_8=Button(root, text="8",padx=10,pady=10,command=lambda:add_number(8))
button_5=Button(root, text="5",padx=10,pady=10,command=lambda:add_number(5))
button_2=Button(root, text="2",padx=10,pady=10,command=lambda:add_number(2))
button_dot=Button(root, text=".",padx=10,pady=10,command=lambda:add_number(7))

button_modulas=Button(root, text="%",padx=10,pady=10,command=lambda:add_number(7))
button_9=Button(root, text="9",padx=10,pady=10,command=lambda:add_number(9))
button_6=Button(root, text="6",padx=10,pady=10,command=lambda:add_number(6))
button_3=Button(root, text="3",padx=10,pady=10,command=lambda:add_number(3))
button_equal=Button(root, text="=",padx=10,pady=10,command=lambda:add_number(7))

button_Ac=Button(root, text="Ac",padx=10,pady=10,command=lambda:add_number(7))
button_divided=Button(root, text="/",padx=10,pady=10,command=lambda:add_number(7))
button_mul=Button(root, text="*",padx=10,pady=10,command=lambda:add_number(7))
button_minas=Button(root, text="-",padx=10,pady=10,command=lambda:add_number(7))
button_plus=Button(root, text="+",padx=10,pady=10,command=lambda:add_number(7))

#plase the buttonz
button_red.grid(row=2,column=0)
button_inv.grid(row=3,column=0)
button_pi.grid(row=4,column=0)
button_e.grid(row=5,column=0)
button_Ans.grid(row=6,column=0)

button_Deg.grid(row=2,column=1)
button_Sin.grid(row=3,column=1)
button_Cos.grid(row=4,column=1)
button_tan.grid(row=5,column=1)
button_Exp.grid(row=6,column=1)

button_X.grid(row=2,column=2)
button_in.grid(row=3,column=2)
button_Log.grid(row=4,column=2)
button_root.grid(row=5,column=2)
button_xY.grid(row=6,column=2)

button_open.grid(row=2,column=3)
button_7.grid(row=3,column=3)
button_4.grid(row=4,column=3)
button_1.grid(row=5,column=3)
button_0.grid(row=6,column=3)

button_close.grid(row=2,column=4)
button_8.grid(row=3,column=4)
button_5.grid(row=4,column=4)
button_2.grid(row=5,column=4)
button_dot.grid(row=6,column=4)

button_modulas.grid(row=2,column=5)
button_9.grid(row=3,column=5)
button_6.grid(row=4,column=5)
button_3.grid(row=5,column=5)
button_equal.grid(row=6,column=5)

button_Ac.grid(row=2,column=6)
button_divided.grid(row=3,column=6)
button_mul.grid(row=4,column=6)
button_minas.grid(row=5,column=6)
button_plus.grid(row=6,column=6)

# Run the Tkinter event loop
root.mainloop()
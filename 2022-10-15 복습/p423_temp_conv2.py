from tkinter import *

window = Tk()

def cc():
    t = e1.get()
    tc = (float(t)-32.0)*5.0/9.0
    e2.delete(0, END)
    e2.insert(0, str(tc))

def ff():
    t = e2.get()
    tf = (float(t)+32)*9.0/5.0
    e1.delete(0, END)
    e1.insert(0, str(tf))

l1 = Label(window, text="화씨")
l2 = Label(window, text="섭씨")

e1 = Entry(window)
e2 = Entry(window)

b1 = Button(window, text="화씨->섭씨", command=cc)
b2 = Button(window, text="섭씨->화씨", command=ff)
l1.grid(row=0, column=0)
l2.grid(row=1, column=0)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
b1.grid(row=2, column=0)
b2.grid(row=2, column=1)

window.mainloop()
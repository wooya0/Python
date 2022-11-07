from tkinter import *

window = Tk()

counter = 0

def clicked():
    global counter
    counter += 1
    label['text'] = '버튼 클릭 횟수: ' + str(counter)

def clear():
    global counter
    counter = 0
    label['text'] = "아직 눌려지지 않음"

label = Label(window, text="아직 눌려지지 않음.")
label.pack()
button1 = Button(window, text="증가", command=clicked)
button2 = Button(window, text="리셋", command=clear)
button1.pack()
button2.pack()
window.mainloop()
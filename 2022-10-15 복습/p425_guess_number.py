from tkinter import *
import random

window = Tk()

answer = random.randint(1, 100)

def ttt():
    global answer
    guess = int(e1.get())
    if guess > answer:
         msg = "높음!"
    elif guess < answer:
        msg = "낮음!"
    else :
        msg = "정답!"
    
    l1['text'] = msg
    e1.delete(0, END)

def clear():
    global answer
    answer = random.randint(1, 100)
    l1['text'] = "1부터 100사이의 숫자를 입력하시오."

window.configure(bg="white")
window.title("숫자를 맞춰보세요!")
window.geometry("500x80")

Label(window, text="숫자 게임에 오신 것을 환영합니다!", bg="white").pack()

e1 = Entry(window)
e1.pack(side=LEFT)

Button(window, text="시도", fg="green", bg="white", command=ttt).pack(side=LEFT)
Button(window, text="초기화", fg="red", bg="white", command=clear).pack(side=LEFT)

l1 = Label(window, text="1부터 100사이의 숫자를 입력하시오.", bg="white")
l1.pack(side=LEFT)

window.mainloop()
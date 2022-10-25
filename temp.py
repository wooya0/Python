#온도 변환 프로그램

from tkinter import *

window = Tk()

def FTC():
    r = (float(F.get()) - 32) * 5/9                                 # 화씨 -> 섭씨 공식
    C.delete(0, END)                                                # 섭씨 Entry 초기화
    C.insert(0, r)                                                  # r 값 입력

def CTF():
    r = (float(C.get()) * 9/5) + 32                                 # 섭씨 -> 화씨 공식
    F.delete(0, END)                                                # 화씨 Entry 초기화
    F.insert(0, r)                                                  # r 값 입력

def clear():                                                        # 전체 초기화
    F.delete(0, END)
    C.delete(0, END)

Label(window, text="화씨").grid(row=0, column=0)                     # 화씨를 입력
F = Entry(window)
F.grid(row=0, column=1)

Label(window, text="섭씨").grid(row=1, column=0)                     # 섭씨를 입력
C = Entry(window)
C.grid(row=1, column=1)

f =Frame(window)
Button(f, text="화씨->섭씨", command=FTC).pack(side=LEFT)       # 화씨를 섭씨를 변경 (함수 : FTC)
Button(f, text="섭씨->화씨", command=CTF).pack(side=LEFT)       # 섭씨를 화씨로 변경 (함수 : CTF)
Button(f, text="초기화", command=clear).pack(side=LEFT)         # 전체 초기화
f.grid(row=2, column=0, columnspan=2)

window.mainloop()

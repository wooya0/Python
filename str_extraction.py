# 문장을 입력하고 범위를 지정하여 슬라이싱 하는 프로그램.
# 시작 범위가 끝 범위 보다 클 경우, 오류 메시지를 출력한다.

from tkinter import *

window = Tk()

def ttt():
    sentence = S.get()
    start = int(StartRange.get())                               # 시작 범위 
    end = int(EndRange.get())                                   # 끝 범위
    if start <= end:                                            # 시작 범위가 끝 범위보다 작을 때
        Result.delete(0, END)                                   # Entry 초기화
        Result.insert(0, sentence[start:end])                   # 문자열을 슬라이싱하여 Result 칸에 입력
    else :                                                      # 시작 범위가 끝 범위보다 클 때 오류 메시지 출력
        Result.delete(0, END)
        Result.insert(0, "잘못 입력하였습니다.")

def AllClear():                                                 # Entry에 담긴 값을 모두 초기화 시킨다.
    S.delete(0, END)
    StartRange.delete(0, END)
    EndRange.delete(0, END)
    Result.delete(0, END)

Label(window, text="글:").grid(row=0, column=0, padx=1)         # 글을 입력 받는다.
S = Entry(window)                                 
S.grid(row=0, column=1, columnspan=3)

Label(window, text="지정한 범위를 추출하는 프로그램").grid(row=1, column=0, columnspan=4)     # 추출 part

Label(window, text="시작 범위:").grid(row=2, column=0)     # 시작 범위를 지정
StartRange = Entry(window, width=3)
StartRange.grid(row=2, column=1)

Label(window, text="끝 범위:").grid(row=2, column=2)       # 끝 범위를 지정
EndRange = Entry(window, width=3)
EndRange.grid(row=2, column=3)

Button(window, text="추출하기", command=ttt).grid(row=3, column=0)      # 범위에 따른 문장을 추출한다.(함수 : ttt)

Button(window, text="전체 초기화", command=AllClear).grid(row=3, column=2)  # 입력 값 전체를 초기화한다. (함수 : AllClear)

Label(window, text="결과:").grid(row=4, column=0)
Result = Entry(window)                                      # 결과값
Result.grid(row=4, column=1, columnspan=3)

window.mainloop()

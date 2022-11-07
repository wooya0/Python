(x,y) = (2,0)
try:
    z = x/y                     # 예외가 발생할 수 잇는 문장
except ZeroDivisionError:
    print("0으로 나누는 예외")   # 예외를 처리하는 문장


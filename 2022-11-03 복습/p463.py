outfile = open("input.txt", "w", encoding="utf-8")
outfile.write("홍길동\n")

try:    # 예외가 발생할 가능성이 있는 작업
    f = open("test.txt", "w") 
    f.write("홍길동")   # 여기서 여러 가지 작업을 한다.
finally:                # 예외가 발생하더라도 반드시 실행한다.
    f.close()

with open("input2.txt", "w", encoding="utf-8") as f:
    f.write("김영희\n")
    f.write("최자영\n")
    # 블록을 빠져나오면 자동으로 파일이 닫쳐진다.
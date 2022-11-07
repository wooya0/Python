infile = open("test.txt", "r+")
str = infile.read(10)
print("읽은 문자열 : ", str)
position = infile.tell()        # 현재 위치
print("현재 위치 : ", position)

position = infile.seek(0)       # 다시 파일의 처음으로
str0 = infile.read(10)
print("읽은 문자열 : ", str)
infile.close()
counter = [0] * 26
infile = open("mobydick.txt", "r")
ch = infile.read(1)
while ch != "":
    ch = ch.upper()                 # 소문자 -> 대문자
    if ch >= "A" and ch <= "Z":
        i = ord(ch) - ord("A")      # 현재 문자의 번호를 알 수 있다.
        counter[i] += 1
    ch = infile.read(1)
print(counter)
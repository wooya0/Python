##
#   이 프로그램은 패스워드를 검사한다.
#
import re
password = input("패스워드를 입력하세요")
flag = 0
while True:
    if len(password) < 8 or not re.search("[A-Z]", password) or re.search("[0-9]", password) or re.search("[a-z]", password) or re.search("[_@$]", password):
        flag = -1
        break
    else:
        flag = 0
        print("유효한 패스워드")
        break

if flag == -1:
    print("유효한 패스워드가 아닙니다.")

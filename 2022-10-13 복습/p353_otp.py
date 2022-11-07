# OTP 발생 프로그램
import random
s = "0123456789"        # 대상 문자열
passlen = 4             # 패스워드 길이

p = "".join(random.sample(s, passlen))      #sample() : 주어진 개수만큼의 글자를 문자열 s에서 임의로 선택
print(p)
# s.capitalize() : 첫 문자만 대문자로 변환 
s = "i am a student."
print(s.capitalize())

# s.lower() : 모든 알파벳 문자를 소문자로 변환
# s.upper() : 모든 알파벳 문자를 대문자로 변환
s = "Breakfast At Tiffany"
print(s.lower())
print(s.upper())

# startswitch(s) : 문자열 s로 시작되는 문자열이면 True가 반환
# endswitch(s) : 문자열 s로 종료되는 문자열이면 True가 반환
s = input("파이썬 소스 파일 이름을 입력하시오: ")
if s.endswith(".py"):
    print("올바른 파일 이름입니다.")
else:
    print("올바른 파일 이름이 아닙니다.")

# replace() : 문자열에서 부분 문자열을 다른 부분 문자열로 변환할 때 사용
s = "www.naver.com"
print(s.replace("com", "co.kr"))

# find() : 대상 문자열 안에서 부분 문자열을 찾아서 인덱스를 반환
print(s.find(".com"))

# s.rfind(<sub>[, <start>[, <end>]]) : 끝에서 시작하여 지정된 부분 문자열을 대상 문자열 안에서 검색
s = "Let it be, let it be, let it be"
print(s.rfind("let"))

# count() : 문자열 중에서 부분 문자열이 등장하는 횟수
s = "www.naver.co.kr"
print(s.count("."))
print(s.count(".", 0, 5))       # s.count("찾을 문자열", 시작 위치, 종료 위치)

# s.isalpha() : 문자열 s 안의 모든 문자가 알파벳이면 True를 반환하고, 그렇지 않으면 False를 반환
# s.isdigit() : 문자열 s가 숫자로만 구성되어 있으면 True를 반환
s = "abce"
print(s.isalpha())
s = "123"
print(s.isdigit())

# strip() : 공백 문자를 제거 / rstrip(), lstrip()
s = "  Hello, World!  "
print(s.strip())

#split() : 문자열 분리
s = "Welcome to Python"
print(s.split())

#join() : 단어들을 모아서 하나의 문자열로 만드는 함수
print(",".join(["apple", "grape", "banana"]))
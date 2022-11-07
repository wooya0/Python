# 중복되지 않은 단어의 개수를 세는 프로그램
txt = input("입력 텍스트: ")
words = txt.split(" ")
unique = set(words)         #집합으로 만들면 자동적으로 중복을 제거

print("사용된 단어의 개수== ",len(unique))
print(unique)
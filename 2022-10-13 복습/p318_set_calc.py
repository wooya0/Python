# 세트 연산
fruits = {"apple", "banana", "grape"}
size = len(fruits)                          #len() : 세트 안에 저장된 요소의 개수
print(size)

if "apple" in fruits:                       #in 연산자 : 어떤 항목이 세트 안에 있는지 검사
    print("집합 안에 apple이 있습니다.")

for x in fruits:
    print(x, end=" ")
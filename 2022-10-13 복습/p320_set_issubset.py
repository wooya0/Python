# 부분집합 연산
A = {"apple", "banana", "grape"}
B = {"apple", "banana", "grape", "kiwi"}

if A < B:   #또는 A.issubset(B) :
    print("A는 B의 부분 집합입니다.")

if A == B:
    print("A와 B는 같습니다.")
else :
    print("A와 B는 같지 않습니다.")
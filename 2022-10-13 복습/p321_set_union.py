A = {"apple", "banana", "grape"}
B = {"apple", "banana", "grape", "kiwi"}

# 합집합
C = A | B       # 또는 C = A.union(B) 

#교집합
C = A & B       # 또는 C = A.intersection(B)

#차집합
C = A - B       # 또는 C = A.difference(B)
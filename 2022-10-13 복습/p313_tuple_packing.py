# 튜플 패킹과 언패킹
x = ("apple", "banana", "grape")        
(s1, s2, s3) = x        #튜플 패킹
print(s1, s2, s3)       #튜플 언패킹

student = ("Kim", [3.1, 3.6, 4.0, 0.0])     #서로 다른 자료형에 대해서도 패킹과 언패킹이 가능
name, grades = student
print(name)
print(grades)
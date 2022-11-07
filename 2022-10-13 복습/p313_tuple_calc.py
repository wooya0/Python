# 튜플 연산
fruits = ("apple", "banana", "grape")
fruits += ("pear", "kiwi")              # += 연산자 : 다른 튜플 추가 가능
print(fruits)

student = ("Kim", [3.1, 3.6, 4.0, 0.0])
student[1][3] = 4.3                         #리스트는 변경 가능
print(student)

numbers = [10, 20, 30]
numbers += (40, 50)         #튜플을 리스트에 추가하는 것은 가능
print(numbers)
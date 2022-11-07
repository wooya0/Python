fruits = {"apple", "banana", "grape"}
# 세트 요소 추가와 삭제
fruits.add("kiwi")          #add() : 요소 추가
print(fruits)

fruits.remove("kiwi")       #remove() : 요소 삭제
print(fruits)

fruits.clear()              #clear() : 모든 요소 삭제
print(fruits)

fruits.update(["orange", "mango", "kiwi"])        #update() : 여러 개의 항목 추가
print(fruits)
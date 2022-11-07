# 딕셔너리 항목 탐색
capitals = {"Korea":"Seoul", "USA":"Washington", "UK":"London"}
for key in capitals :
    print(key, end=" ")     #키만 내보냄

for key in capitals :
    print(key, ":", capitals[key])      #dictionary[key] : 값 추출

for key, value in capitals.items():
    print(key, ":", value)

    
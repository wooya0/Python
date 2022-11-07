from os import cpu_count


# 딕셔너리 항목 추가
capitals = {}
capitals["Korea"] = "Seoul"
capitals["USA"] = "Washington"
capitals["UK"] = "London"
capitals["France"] = "Paris"
print(capitals)

capitals.update({"Japen":"Tokyo", "Germany":"Berlin"})      #update() : 다른 딕셔너리 전체를 현재 딕셔너리에 추가
print(capitals)
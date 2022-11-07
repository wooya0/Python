try:
    f = open("test1.txt", "w", encoding='utf-8')
    f.write("테스트 데이터를 파일에 습니다!!")
except IOError:
    print("Error : 파일을 찾을 수 없거나 데이터를 쓸 수 없습니다.")
finally:
    f.close()
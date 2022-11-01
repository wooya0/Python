# 한국돈을 입력하면 외국화폐로 환전계산 하는 프로그램
import pickle

# exrate.pic 파일 제작
# exrate = {"미국" : [1423.0, "달러"], "유럽" : [1408.9, "유로"], "중국" : [194.0, "위안"]}
# f = open("exrate.pic", "wb")
# pickle.dump(exrate, f)
# f.close()

while True:
    f = open("exrate.pic", "rb")    # 이진 파일 오픈
    d = pickle.load(f)              # 피클 파일에 딕셔너리를 로딩
    user_choice = int(input("정수 입력(1.환전, 2.환율정보, 3.국가추가, 4.종료) : "))    #input 화면
    if user_choice == 1:
        print("환전을 시작합니다.")
        country = input("환전할 국가를 입력하시오. ")
        if country in d:                                            # 입력한 국가가 딕셔너리 안에 있을 경우
            money = float(input("바꿀 한국돈을 입력하시오. "))
            r = money / float(d[country][0])                        # 환율 계산
            print(f"{round(r, 2)} {d[country][1]} 환전되었습니다.")
        else:                                                       # 입력한 국가가 딕셔너리 안에 없을 경우
            print("입력한 국가의 정보가 없습니다.")
    elif user_choice == 2:
        print("환율 정보를 출력합니다.")
        print(d)                                                    # 딕셔너리 출력
    elif user_choice == 3:
        print("국가를 추가합니다.")
        country = input("국가를 입력하시오. ")                       # key
        money = float(input("환율을 입력하시오. "))                  # values1
        dan = input("단위를 입력하시오. ")                           # values2
        o = open("exrate.pic", "wb")                                # 이진 파일 오픈
        d[country] = [money, dan]                                   # 딕셔너리 추가
        pickle.dump(d, o)                                           # 피클 파일에 저장
        o.close()                                                   # 파일 닫기 
        print("국가를 추가하였습니다.")
    elif user_choice == 4:
        print("프로그램을 종료합니다.")                              # 무한 루프 탈출
        break
    else:
        print("정수를 잘못 입력하였습니다.")

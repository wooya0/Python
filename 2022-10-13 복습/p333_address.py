#연락처 프로그램

from audioop import add
from pickle import ADDITEMS
from re import A


def main():
    address_book = {}                                   # 공백 딕셔너리를 생성
    while True:                                         # 항상 참
        user = display_menu()
        if user == 1:
            name, number = get_contact()
            address_book[name] = number                 # name과 number를 추가
        elif user == 2:
            name, number = get_contact()
            address_book.pop(name)                      # name을 키로 가지고 항목을 삭제
            print(name,"의 연락처를 삭제하였습니다.")
        elif user == 3:
            name = input("이름 : ")                     # name을 입력 받아 value 값을 출력
            print("연락처 : ",address_book[name])
        elif user == 4:
            for key in sorted(address_book):            # 딕셔너리를 정렬하여 출력
                print(key,"의 전화번호:",address_book[key])
        elif user == 5:                                 # 무한 루프 탈출
            break
        else: 
            print("잘못입력하셨습니다.")        

            

def display_menu():
    print("1. 연락처추가\n2. 연락처 삭제\n3. 연락처 검색\n4. 연락처 출력\n5. 종료")
    select = int(input("메뉴 항목을 선택하시오: "))
    return select
def get_contact():
    name = input("이름 : ")
    number = input("전화번호 : ")
    return name, number

main()
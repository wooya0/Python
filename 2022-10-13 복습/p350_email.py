# 이메일 주소에서 아이디와 도메인을 구분
address = input("이메일 주소를 입력하시오: ")
(id, domain) = address.split("@")

print(address)
print("아이디:"+id)
print("도메인:"+domain)
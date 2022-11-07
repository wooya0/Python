import csv      # CSV 모듈을 불러온다

f = open("weather.csv")     # CSV 파일을 열어서 f에 저장한다.
data = csv.reader(f)        # reader() 함수를 이용하여 읽는다.
cold = 100
for row in data:            # 반복 루프를 사용하여 데이터를 읽는다.
    if cold >= float(row[3]):
        cold = float(row[3])
        day = row[0].split('-')

print(f"{day[0]}년 {day[1]}월 {day[2]}일이 {cold}도로 가장 추웠습니다.")

f.close()
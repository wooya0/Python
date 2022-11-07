import os

cwd = os.getcwd()       # 작업 리렉토리 변경
files = os.listdir()    # 작업 디렉토리 안에 있는 파일들의 리스트 얻음
for name in files :
    if os.path.isfile(name):    # listdir() 함수에서 파일만 처리하는 함수
        if name.endswith(".txt"):   #파일 확장자 검색
            print(name)

import pickle
game0ption = {      # 파일을 닫는다.
    "Sound" : 8,
    "VideoQuality" : "HIGH",
    "Money" : 100000,
    "WeaponList" : ["gun","missile","knife"]
}

file = open("save.p", "wb")         # 이진 파일 오픈
pickle.dump(game0ption, file)       # 딕셔너리를 피클 파일에 저장
file.close()                        # 파일을 닫는다.
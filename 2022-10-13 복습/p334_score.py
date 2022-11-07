# 학생 성적 처리
score_dic = {
    "Kim" : [99, 83, 95],
    "Lee" : [68, 45, 78],
    "Choi" : [25, 56, 69]}

for name, scores in score_dic.items():
    print(name,"의 평균 성적=",round(sum(scores)/len(scores), 2))

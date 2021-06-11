maxScore = int(input("テストの上限点数"))
answer_score = maxScore / 2

# Xは正解の点数
correct_answer = 83

x = 1

while not correct_answer == answer_score:
    if answer_score > correct_answer:
        score = round((correct_answer - answer_score) / 2)
    elif answer_score < correct_answer:
        score = round((answer_score - correct_answer) / 2)

    answer_score = correct_answer - score

    if correct_answer == score:
        pass
    elif correct_answer > score:
        x += 1
    else:
        x += 1
print(x)

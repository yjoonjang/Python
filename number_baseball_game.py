answer = input("0~9 사이의 숫자를 연속으로 입력하시오 (중복입력 금지) :")
for i in range(len(answer)):
    if answer[i] in answer[i+1:]:
        print("중복입력하셨습니다. 다시 입력해 주세요")
        break;
predict = input("예상되는 0~9 사이의 숫자를 연속으로 입력하시오 (중복입력 금지):")
for i in range(len(predict)):
    if predict[i] in predict[i+1:]:
        print("중복입력하셨습니다. 다시 입력해 주세요")
        break;
    else: 
        strike = 0
        ball = 0
        out = 0
for i in range(len(answer)):
    if answer[i] == predict[i]:
        strike += 1
    elif predict[i] in answer:
        ball += 1
    else:
        out += 1

if out == len(answer):
    print("OUT")
else:
    print("{0}STRIKE {1}BALL".format(strike, ball))



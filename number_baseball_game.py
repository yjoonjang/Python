answer = input("0~9 사이의 숫자를 연속으로 입력하시오 (중복입력 금지) :")
predict = input("예상되는 0~9 사이의 숫자를 연속으로 입력하시오 (중복입력 금지):")
strike = 0
ball = 0
out = 0

for i in range(len(answer)):
    if answer[i] == predict[i]:
        strike += 1
    elif predict[i] in answer:
        ball += 1
    elif predict[i] not in answer:
        out += 1

if out == len(answer):
    print("OUT")
else:
    print("{0}STRIKE {1}BALL".format(strike, ball))

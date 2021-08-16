sentence = str(input("문자열을 입력해 주세요:")) + ' ' # 문자열을 입력받음 -> 마지막을 공백으로 처리하면 for 문에서 마지막에 값을 비교할 때 다르게 판별 가능
focus_ch = sentence[0] # 처음에 집중하는 문자 = 배열의 첫째항
count = 1 # 처음에 카운트 = 1로 설정
for character in sentence[1:]: # 첫째항을 제외한 리스트에 있는 모든 값들에 대해
    if focus_ch == character: # 현재 집중하고 있는 문자가 리스트에 있는 문자이면
        count += 1 # 카운트를 하나 증가시킴
    else:  # 집중하고 있는 문자가 현재 리스트에 있는 문자와 다르면
        print(focus_ch+str(count),end="" ) # 현재 집중하는 문자, 그동안의 카운트 수 출력
        count = 1 # 카운트 = 1로 재설정
        focus_ch = character # 집중하고 있는 문자 = 현재 보고 있는 문자로 재설정

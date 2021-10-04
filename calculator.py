calculation = list(input("계산을 입력하세요: ")) # 222+123+12+234-2342
add_list = [] #더할 값들이 들어갈 리스트
subtract_list = [] #뺄 값들이 들어갈 리스트
threshold = 1 #초기설정 : 한계범위 = 1
add_list_joined = [] #후에 더할 값들이 '' 없는 상태로 들어갈 리스트
subtract_list_joined = [] #후에 뺄 값들이 '' 없는 상태로 들어갈 리스트
result = 0 #최종결과

if calculation[0] == '-' : #리스트의 처음값이 음수인 경우
    calculation.append('') #맨 끝에 여백을 더함 (마지막 문자 처리를 위해)
else : #처음 값이 양수인 경우
    calculation.insert(0,'+') #처음에 + 기호를 더함 (더할 숫자임을 알리기 위해) -> 변환된 값 : +222+123+12+234-2342
    calculation.append('') 

for i in range(len(calculation)) : 
    if calculation[i] == '+' : #기호가 +일 때
        while True : #threshold 값 증가를 위해 무한루프 생성
            if calculation[(i + threshold)] == '+' or calculation[(i + threshold)] == '-' or calculation[(i + threshold)] == "" : #처음 기호 나온 후 다음 기호(또는 여백) 나올 때
                add_list.append(calculation[(i+1) : (i+threshold)]) #'+' 뒤에 숫자부터 다음 기호 나오기 전 숫자를 add_list에 더함
                threshold = 1 #threshold = 1로 초기화
                break; #무한루프 탈출 
            else : #처음 기호 나온 후에 기호가 나오지 않았을 때
                threshold += 1
    elif calculation[i] == '-' : #기호가 -일 때
        while True :
            if calculation[(i + threshold)] == '+' or calculation[(i + threshold)] == '-' or calculation[(i + threshold)] == "" :
                subtract_list.append(calculation[(i+1) : (i+threshold)])
                threshold = 1
                break;
            else :
                threshold += 1

for i in range(len(add_list)) :
    add_list_joined.append(''.join(add_list[i])) #''없는 값들을 add_list_joined에 더함
    result = result + int(add_list_joined[i]) #결과에서 더함
for i in range(len(subtract_list)) :
    subtract_list_joined.append(''.join(subtract_list[i]))
    result = result - int(subtract_list_joined[i]) #결과에서 뺌

print(result)
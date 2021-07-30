# 문자열을 입력받는다.
# 변수 count=0을 지정
# 각 알파벳에 대한 for 문을 알파벳의 길이만큼 돌림 // 이유: sentence[i] 와 알파벳을 비교하기 위해
# 알파벳이 바뀌면 원래 다루고 있던 알파벳과 count를 출력하고, count=1로 초기화한다
sentence = str(input("문자열을 입력해 주세요:")) #aabbaa 012345

count = 0
ch = sentence[0] #ch = a
for i in range(len(sentence)):  #sentence[i]와 알파벳을 비교하기위해
    if sentence[i] == ch:  # 현재 중점을 두는 문자와 일치하는 지를 보기 위해
        if i == len(sentence)-1:
            count += 1 
            print(ch,count)
        else: count += 1 
        
    elif sentence[i] != ch: #현재 중점을 두는 문자와 일치하지 않으면 count 값을 1로 초기화하고 중점을 두는 문자도 초기화하기 위해
        if i == len(sentence)-1:
            print(ch, count)
            count = 1
            ch = sentence[i]
            print(ch, count)
        else: 
            print(ch, count)
            count = 1
            ch = sentence[i]




    

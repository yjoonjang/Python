array = [1, 10, 5, 8, 7, 6, 4, 3, 2, 9]
for i in range(10) :
    min = 9999 # 반복할 때마다 min을 9999로 초기화시켜 주기 위해 for문 안쪽에 정의함                        
    for j in range(i,10) :
        if (min > array[j]) : 
            min = array[j] # array에서 고른 값 중 가장 작은 값을 min으로 정의함
            index = j # index에 j값을 부여함
    #스와핑 -> 가장 작은 값은 가장 앞에, 원래 앞에 있었던 값은 원래 가장 작은 값이 있었던 자리로 이동함
    temp = array[i] 
    array[i] = array[index] 
    array[index] = temp

print(array)

# 배운 점
# 1. i,j를 이용하여 뒤의 값을 하나씩 검사하는 방법
# 2. swapping(스와핑) 을 통해 값(위치)를 바꿈

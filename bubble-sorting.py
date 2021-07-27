# #1.

# 숫자 n이 주어지고, n 개 만큼 무작위 수(0 <= x <= 100000)가 주어진다. 이를 내림차순으로 정렬하여 출력하여라.

# > 5
# > 22 31 42 50 12
# 50
# 42
# 31
# 22
# 12

n = int(input("작성할 수의 개수를 입력하시오: "))
lst=[]
i = 0
while (i<n):
    a = int(input("수를 입력하시오: "))
    lst.append(a)
    i += 1

for k in range(1, n+1):
    for i in range(n-k):
        if lst[i] < lst[i+1]:
            lst[i],lst[i+1] = lst[i+1],lst[i]


for i in range(n):
    print(lst[i])

# 왜 a = int()로 감싸지 않으면 첫째자리 수들만 인식이 되는가 ?







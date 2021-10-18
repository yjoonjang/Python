from collections import deque

num_set = set(range(1,10001))
non_self_number_list = deque()

def d(n) :
    sum = n
    for i in range(len(str(n))) :
        sum += int(str(n)[i])
    return sum

for i in range(1,10000) :
    while d(i) <= 10000 :
        non_self_number_list.append(d(i))
        i += 1

non_self_number_set = set(non_self_number_list)
self_number_list = list(num_set - non_self_number_set)
print(sorted(self_number_list))

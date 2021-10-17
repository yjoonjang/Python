input = input("단어를 입력해 주세요: ").upper() #ZZA  Mississipi
input_set = set(input)
word_count_list = []
count_list = []
count = 0
count_max = 0

for word in input_set :
    for i in range(len(input)) :
        if word == input[i] :
            count += 1
        if i == len(input)-1 :
            word_count = word + str(count)
            word_count_list.append(word_count)
            count = 0

for i in range(len(word_count_list)) :
    b = word_count_list[i]
    count_list.append(b[1])
for i in range(len(count_list)) :
    if max(count_list) == count_list[i] :
        count_max += 1
if count_max != 1 :
    print("?")
else:
    k = word_count_list[count_list.index(max(count_list))]
    print(k[0])

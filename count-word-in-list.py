input = input("문자열을 작성하시오 :") #ljes=njak -> 9자리 ddz=z=
answer_list = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

# 방법 1
# for answer_word in answer_list:
#     input = input.replace(answer_word, '*')
# print(len(input))

#방법 2
count = len(input)

for i in range (len(answer_list)) :
    if answer_list[i] in input :
        if len(answer_list[i]) == 3 :
            count -= 2
            # input[input.index(answer_list[i]) : input.index(answer_list(i))+3]
        elif len(answer_list[i]) == 2 :
            count -= 1


print(count)


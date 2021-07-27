from datetime import datetime
today = datetime.today().strftime("%Y%m%d") 

D_day = input("예정된 날의 연월일을 입력하시오: ") # 원하는 연월일을 입력받음

D_day_y = int(D_day[:4]) 
D_day_m = int(D_day[4:6])
D_day_d = int(D_day[6:])
today_y = int(today[:4])
today_m = int(today[4:6])
today_d = int(today[6:])
# D_day_(y,m,d) 는 각각 입력연도, 입력월, 입력일
# today_(y,m,d) 는 각각 오늘연도, 오늘월, 오늘일

date = 0 # 구하려는 최종 일수
date_pass = 0 # 지나간 최종 일수

# year_to_day : 연도 사이를 일수로 바꾸어주는 변수
y_list=[] # 연도를 포함하는 리스트를 생성
yoon_count = 0 # 현재년도와 마감년도 사이에 윤년이 몇 번 있었는지 세는 변수
if today_y < D_day_y: 
    for i in range(today_y, D_day_y): # (현재년도+1 <= i < 입력년도) 인 모든 정수 i 에 대해
        y_list.append(i) # 그 수들을 y_list에 추가한다
    for year in y_list: # 리스트에 있는 년도들 중 
        if year % 4 == 0: # 년도가 4의 배수면
            yoon_count += 1 # 윤년을 세는 변수에 1을 더함
else: 
    for i in range(D_day_y, today_y): # (입력년도 <= i < 현재년도) 인 모든 정수 i 에 대해: [i는 입력년도 ~ (현재년도-1) 사이의 정수]
        y_list.append(i) # 그 수들을 y_list에 추가한다
    for year in y_list: # 리스트에 있는 년도들 중 
        if year % 4 == 0: # 년도가 4의 배수면
            yoon_count += 1 # 윤년을 세는 변수에 1을 더함
year_to_day = 365 * (len(y_list) - yoon_count) + 366 * yoon_count # 365 * (리스트 크기 - 윤년의 수) + 366 * 윤년의 수

if today_y % 4 == 0: # 현재연도가 윤년이라면
    if D_day_y == today_y: # 입력년도 = 현재년도
        if D_day_m > today_m: # 입력월 > 현재월
            for i in range(today_m, D_day_m): # (현재월 <= i < 입력월)인 모든 정수 i 에 대해
                if i == 2: # 윤년인 해의 2월의 최대 일수는 29일
                    date += 29
                elif i in ['1', '3', '5', '7', '8', '10', '12']: # 최대 일수가 31일 인 월들
                    date += 31
                else: # 최대 일수가 30일
                    date += 30
            date = date - today_d + D_day_d 
            print("D-{}".format(date))

        elif D_day_m == today_m: # 입력월 = 현재월
            if D_day_d > today_d: # 입력한 날의 일 > 현재의 일
                date = D_day_d - today_d
                print("D-{}".format(date))
            elif D_day_d == today_d: # 입력한 날의 일 = 현재의 일
                print("D-day")
            else: # 입력한 날의 일 < 현재 일
                date = today_d - D_day_d
                print("D+{}".format(date))

        else: # 입력월 < 현재월
            for i in range(D_day_m, today_m): # (입력월 <= i < 현재월)을 만족하는 모든 정수 i에 대해
                if i == 2: # 윤년인 해의 2월의 최대 일수는 29일
                    date += 29
                elif i in ['1', '3', '5', '7', '8', '10', '12']: # 최대 일수가 31일 인 월들
                    date += 31
                else: # 최대 일수가 30일
                    date += 30
            date = date - D_day_d + today_d
            print("D+{}".format(date))

## 계산 방법 : ex. 현재: 20210722 / 입력 : 20240219
## year_to_day를 사용하면 20210101 부터 20231231 까지의 일수를 구할 수 있음
## year_to_day에서 (20210721 - 20210101 +1)만큼의 일수를 뺌
## 빼고 (20240219 - 20240101 + 1) 만큼의 일수를 더함
    elif D_day_y > today_y: # 입력연도 > 현재연도(현재연도는 여전히 윤년임)
        if D_day_y % 4 == 0: # 입력연도가 윤년일 때
            for i in range(D_day_m): # (현재월 <= i < 입력월)인 모든 정수 i 에 대해
                if i == 2: # 윤년인 해의 2월의 최대 일수는 29일
                    date += 29
                elif i in ['1', '3', '5', '7', '8', '10', '12']: # 최대 일수가 31일 인 월들
                    date += 31
                else: # 최대 일수가 30일
                    date += 30
            for i in range(today_m):
                if i == 2: # 윤년인 해의 2월의 최대 일수는 29일
                    date_pass += 29
                elif i in ['1', '3', '5', '7', '8', '10', '12']: # 최대 일수가 31일 인 월들
                    date_pass += 31
                else: # 최대 일수가 30일
                    date_pass += 30
            date = year_to_day + date - date_pass - today_d + D_day_d
            print("D-{}".format(date))
        else: #입력연도가 윤년이 아닐 때 / ex. 입력연도 20290819
            for i in range(D_day_m): # (현재월 <= i < 입력월)인 모든 정수 i 에 대해
                if i == 2: # 윤년이 아닌 해의 2월의 최대 일수는 28일
                    date += 28
                elif i in ['1', '3', '5', '7', '8', '10', '12']: # 최대 일수가 31일 인 월들
                    date += 31
                else: # 최대 일수가 30일
                    date += 30
            for i in range(today_m):
                if i == 2: # 윤년인 해의 2월의 최대 일수는 29일
                    date_pass += 29
                elif i in ['1', '3', '5', '7', '8', '10', '12']: # 최대 일수가 31일 인 월들
                    date_pass += 31
                else: # 최대 일수가 30일
                    date_pass += 30
            date = year_to_day + date - date_pass - today_d + D_day_d
            print("D-{}".format(date))
    
    else: # 입력연도 < 현재연도(현재연도는 여전히 윤년임) /  ex. 현재연도 : 20240210 // 입력연도 : 20200419
        if D_day_y % 4 == 0: # 입력연도가 윤년일 때
            for i in range(D_day_m): # (i < 입력월)인 모든 정수 i 에 대해
                if i == 2: # 윤년인 해의 2월의 최대 일수는 29일
                    date += 29
                elif i in ['1', '3', '5', '7', '8', '10', '12']: # 최대 일수가 31일 인 월들
                    date += 31
                else: # 최대 일수가 30일
                    date += 30
            for i in range(today_m):
                if i == 2: # 윤년인 해의 2월의 최대 일수는 29일
                    date_pass += 29
                elif i in ['1', '3', '5', '7', '8', '10', '12']: # 최대 일수가 31일 인 월들
                    date_pass += 31
                else: # 최대 일수가 30일
                    date_pass += 30
            date = year_to_day - date + date_pass + today_d - D_day_d
            print("D+{}".format(date))
        else: #입력연도가 윤년이 아닐 때  ex. 입력연도 20210819 // 현재연도 20240210
            for i in range(D_day_m): # (현재월 <= i < 입력월)인 모든 정수 i 에 대해
                if i == 2: # 원래 2월의 일수는 28일
                    date += 28
                elif i in ['1', '3', '5', '7', '8', '10', '12']: # 최대 일수가 31일 인 월들
                    date += 31
                else: # 최대 일수가 30일
                    date += 30
            for i in range(today_m):
                if i == 2: # 윤년인 해의 2월의 최대 일수는 29일
                    date_pass += 29
                elif i in ['1', '3', '5', '7', '8', '10', '12']: # 최대 일수가 31일 인 월들
                    date_pass += 31
                else: # 최대 일수가 30일
                    date_pass += 30
            date = year_to_day - date + date_pass + today_d - D_day_d
            print("D+{}".format(date))

else: # 현재연도가 윤년이 아니라면
    if D_day_y == today_y: # 입력년도 = 현재년도
        if D_day_m > today_m: # 입력월 > 현재월
            for i in range(today_m, D_day_m): # (현재월 <= i < 입력월)인 모든 정수 i 에 대해
                if i == 2: # 윤년이 아니므로 해의 2월의 최대 일수는 28일
                    date += 28
                elif i in ['1', '3', '5', '7', '8', '10', '12']: # 최대 일수가 31일 인 월들
                    date += 31
                else: # 최대 일수가 30일
                    date += 30
            date = date - today_d + D_day_d 
            print("D-{}".format(date))

        elif D_day_m == today_m: # 입력월 = 현재월
            if D_day_d > today_d: # 입력한 날의 일 > 현재의 일
                date = D_day_d - today_d
                print("D-{}".format(date))
            elif D_day_d == today_d: # 입력한 날의 일 = 현재의 일
                print("D-day")
            else: # 입력한 날의 일 < 현재 일
                date = today_d - D_day_d
                print("D+{}".format(date))

        else: # 입력월 < 현재월
            for i in range(D_day_m, today_m): # (입력월 <= i < 현재월)을 만족하는 모든 정수 i에 대해
                if i == 2: # 윤년이 아닌 해의 2월의 최대 일수는 28일
                    date += 28
                elif i in ['1', '3', '5', '7', '8', '10', '12']: # 최대 일수가 31일 인 월들
                    date += 31
                else: # 최대 일수가 30일
                    date += 30
            date = date - D_day_d + today_d
            print("D+{}".format(date))


    elif D_day_y > today_y: # 입력연도 > 현재연도(현재연도는 여전히 윤년 아님)
        if D_day_y % 4 == 0: # 입력연도가 윤년일 때
            for i in range(D_day_m): # (현재월 <= i < 입력월)인 모든 정수 i 에 대해
                if i == 2: # 윤년인 해의 2월의 최대 일수는 29일
                    date += 29
                elif i in ['1', '3', '5', '7', '8', '10', '12']: # 최대 일수가 31일 인 월들
                    date += 31
                else: # 최대 일수가 30일
                    date += 30
            for i in range(today_m):
                if i == 2: # 윤년이 아닌 해의 2월의 최대 일수는 28일
                    date_pass += 28
                elif i in ['1', '3', '5', '7', '8', '10', '12']: # 최대 일수가 31일 인 월들
                    date_pass += 31
                else: # 최대 일수가 30일
                    date_pass += 30
            date = year_to_day + date - date_pass - (today_d+1) + D_day_d
            print("D-{}".format(date))
        else: #입력연도가 윤년이 아닐 때 
            for i in range(D_day_m): # (현재월 <= i < 입력월)인 모든 정수 i 에 대해
                if i == 2: # 윤년이 아닌 해의 2월의 최대 일수는 28일
                    date += 28
                elif i in ['1', '3', '5', '7', '8', '10', '12']: # 최대 일수가 31일 인 월들
                    date += 31
                else: # 최대 일수가 30일
                    date += 30
            for i in range(today_m):
                if i == 2: # 윤년이 아닌 해의 2월의 최대 일수는 28일
                    date_pass += 28
                elif i in ['1', '3', '5', '7', '8', '10', '12']: # 최대 일수가 31일 인 월들
                    date_pass += 31
                else: # 최대 일수가 30일
                    date_pass += 30
            date = year_to_day + date - date_pass - today_d + D_day_d
            print("D-{}".format(date))
    
    else: # 입력연도 < 현재연도(현재연도는 여전히 윤년 아님) ex. 현재연도 : 20240210 // 입력연도 : 20200419
        if D_day_y % 4 == 0: # 입력연도가 윤년일 때
            for i in range(D_day_m): # (i < 입력월)인 모든 정수 i 에 대해
                if i == 2: # 윤년인 해의 2월의 최대 일수는 29일
                    date += 29
                elif i in ['1', '3', '5', '7', '8', '10', '12']: # 최대 일수가 31일 인 월들
                    date += 31
                else: # 최대 일수가 30일
                    date += 30
            for i in range(today_m):
                if i == 2: # 윤년이 아닌 해의 2월의 최대 일수는 28일
                    date_pass += 28
                elif i in ['1', '3', '5', '7', '8', '10', '12']: # 최대 일수가 31일 인 월들
                    date_pass += 31
                else: # 최대 일수가 30일
                    date_pass += 30
            date = year_to_day - date + date_pass + today_d - D_day_d
            print("D+{}".format(date))
        else: #입력연도가 윤년이 아닐 때  
            for i in range(D_day_m): # (i < 입력월)인 모든 정수 i 에 대해
                if i == 2: # 원래 2월의 일수는 28일
                    date += 28
                elif i in ['1', '3', '5', '7', '8', '10', '12']: # 최대 일수가 31일 인 월들
                    date += 31
                else: # 최대 일수가 30일
                    date += 30
            for i in range(today_m):
                if i == 2: # 윤년이 아닌 해의 2월의 최대 일수는 28일
                    date_pass += 28
                elif i in ['1', '3', '5', '7', '8', '10', '12']: # 최대 일수가 31일 인 월들
                    date_pass += 31
                else: # 최대 일수가 30일
                    date_pass += 30
            date = year_to_day - date + date_pass + today_d - D_day_d
            print("D+{}".format(date))


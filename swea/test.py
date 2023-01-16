# 입력 예시
# 2015
# 8
# 31

# 출력 예시
#경고 월요일입니다.
#{'년': 2015, '월': 8, '일': 31, '요일': '월요일'}

import calendar

ans = dict()

while True:
    year = int(input())
    if calendar.isleap(year) == True:
        print("윤년입니다. 연도를 다시 입력해주세요.")

    else:
        print(calendar.calendar(year))
        ans['년'] = year
        break

month = int(input())
ans['월'] = month
day = int(input())
ans['일'] = day
weekday = calendar.weekday(year, month, day)


if weekday == 0:
    ans['요일'] = '월요일'
    print("경고 월요일입니다.")

elif weekday == 1:
    ans['요일'] = '화요일'

elif weekday == 2:
    ans['요일'] = '수요일'

elif weekday == 3:
    ans['요일'] = '목요일'

elif weekday == 4:
    ans['요일'] = '금요일'

elif weekday == 5:
    ans['요일'] = '토요일'

elif weekday == 6:
    ans['요일'] = '일요일'

print(ans)
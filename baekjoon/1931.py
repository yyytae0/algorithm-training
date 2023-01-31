from sys import stdin


ip = int(stdin.readline())
timetable = {}
same = list()

for i in range(ip):
    dummy = list(map(int, stdin.readline().split()))
    if dummy[1] in timetable.keys():
        if dummy[0] == dummy[1]:
            same.append(dummy[0])

        elif dummy[0] > timetable[dummy[1]]:
            timetable[dummy[1]] = dummy[0]

    else:
        if dummy[0] == dummy[1]:
            same.append(dummy[0])

        else:
            timetable[dummy[1]] = dummy[0]

finish = list(timetable.keys())
if len(finish) != 0:
    dummy_cnt = 0
    cnt = 1
    finish.sort()
    dummy = finish[0]

    if timetable[dummy] in same:
        cnt += 1

    if dummy in same:
        cnt += 1

    for i in finish:
        if dummy_cnt == 0:
            dummy_cnt = 1
            continue

        if dummy > timetable[i]:
            continue

        else:
            dummy = i
            print(dummy)
            if dummy in same:
                cnt += 1
            cnt += 1

    print(cnt)

else:
    print(len(same))


# 반례
# 8
# 1 3
# 2 3
# 3 3
# 4 4
# 5 5
# 6 6
# 7 7
# 3 6

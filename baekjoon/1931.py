from sys import stdin


ip = int(stdin.readline())
timetable = {}
same = list()

for i in range(ip):
    dummy = list(map(int, stdin.readline().split()))
    key = []
    if dummy[1] in key:
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

    for i in finish:
        if dummy_cnt == 0:
            dummy_cnt = 1
            continue

        if dummy > timetable[i]:
            continue

        else:
            for j in range(dummy, timetable[i]+1):
                if j in same:
                    cnt += 1
            dummy = i
            cnt += 1
            print(dummy, 1)

    print(cnt, 2)

else:
    print(len(same), 3)


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
#
# import sys
# N = int(sys.stdin.readline())
# arr = [list(map(int, sys.stdin.readline().split()))for _ in range(N)]
# arr.sort(key = lambda x:(x[1], x[0]))
# cnt = 1
# fin = arr[0][1]
# for i in range(1,N):
#     if fin <= arr[i][0]:
#         cnt += 1
#         fin = arr[i][1]
# print(cnt)

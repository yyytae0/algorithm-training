from sys import stdin


ip = int(stdin.readline())
timetable = {}

for i in range(ip):
    dummy = list(map(int, stdin.readline().split()))
    if dummy[1] in timetable.keys():
        if dummy[0] > timetable[dummy[1]]:
            timetable[dummy[1]] = dummy[0]

    else:
        timetable[dummy[1]] = dummy[0]

finish = list(timetable.keys())
dummy_cnt = 0
cnt = 1
finish.sort()
dummy = finish[0]
for i in finish:
    if dummy_cnt == 0:
        dummy_cnt = 1
        continue

    if dummy > timetable[i]:
        continue

    else:
        dummy = i
        cnt += 1

print(cnt)
# 반례
# 5
# 6 7
# 6 6
# 5 6
# 5 5
# 7 7

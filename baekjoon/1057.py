ip = list(map(int, input().split()))
cnt_1 = 0
cnt_2 = 0


for i in range(18):
    if ip[1] >= 2 ** i:
        cnt_1 = i

    if ip[2] >= 2 ** i:
        cnt_2 = i

    if (ip[1] <= 2 ** i) and (ip[2] <= 2 ** i):
        break

print(cnt_1, cnt_2)
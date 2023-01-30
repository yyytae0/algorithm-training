a, b = map(int, input().split())
cnt = {2: 0, 5: 0}
b_lst = []
c_lst = []
for i in range(1, a + 1):
    if i % 5 == 0:
        dummy = i
        while dummy % 5 == 0:
            cnt[5] += 1
            dummy = dummy // 5

    if i % 2 == 0:
        dummy = i
        while dummy % 2 == 0:
            cnt[2] += 1
            dummy = dummy // 2

    if i == b:
        b_lst = [cnt[2], cnt[5]]

    if i == a - b:
        c_lst = [cnt[2], cnt[5]]

print(min(cnt[2] - c_lst[0] - b_lst[0], cnt[5] - c_lst[1] - b_lst[1]))

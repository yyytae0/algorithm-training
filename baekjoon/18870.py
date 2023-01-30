ip = int(input())
lst = list(map(int, input().split()))
dummy_lst = lst[:]
dummy_lst.sort()
dummy = -1000000001
cnt = dict()
dummy_cnt = 0
for i in dummy_lst:
    if i != dummy:
        cnt[i] = dummy_cnt
        dummy = i
        dummy_cnt += 1

ans = list()
for i in lst:
    ans.append(cnt[i])

print(*ans)

n = int(input())
lst = list(map(int, input().split()))
cnt = [0 for _ in range(n)]
ans = 0
for i in range(n):
    cnt[i] = 1
    for j in range(i):
        if lst[i] > lst[j] and cnt[i] <= cnt[j]:
            cnt[i] = cnt[j]+1
    if ans < cnt[i]:
        ans = cnt[i]
print(ans)

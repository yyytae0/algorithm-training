cost = list(map(int, input().split()))
cnt = [0 for _ in range(101)]
for i in range(3):
    s, g = map(int, input().split())
    for j in range(s, g):
        cnt[j] += 1
ans = 0
for i in range(1, 101):
    if cnt[i]:
        ans += cost[cnt[i]-1]*cnt[i]
print(ans)

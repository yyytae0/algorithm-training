target = [1, 1, 2, 2, 2, 8]
lst = list(map(int, input().split()))
ans = [0 for _ in range(6)]
for i in range(6):
    ans[i] = target[i] - lst[i]

print(*ans)

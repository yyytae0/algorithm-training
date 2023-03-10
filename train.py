def check(a):
    for i in lst[a]:
        d.append(i)
        check(i)


n = int(input())
dp = [0 for _ in range(n+1)]
ans = [0 for _ in range(n+1)]
lst = [[] for _ in range(n+1)]
for i in range(1, n+1):
    dummy = list(map(int, input().split()))
    dp[i] = dummy[0]
    ans[i] = dummy[0]
    if dummy[1] != -1:
        lst[i].append(dummy[1])
d = []
for i in range(1, n+1):
    d = []
    check(i)
    for j in d:
        ans[i] += dp[j]

for i in range(1, n+1):
    print(ans[i])

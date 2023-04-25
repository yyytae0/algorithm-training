def check():
    global idx
    for i in range(1, n):
        if lst[i] > dp[idx]:
            idx += 1
            dp[idx] = lst[i]
        else:
            solve(lst[i])
        print(*dp)


def solve(t):
    s = 0
    g = idx
    while s != g:
        mid = (s+g)//2
        if dp[mid] > t:
            g = mid
            pass
        else:
            s = mid+1
    dp[s] = t


n = int(input())
lst = list(map(int, input().split()))
dp = [0 for _ in range(n)]
dp[0] = lst[0]
idx = 0
check()
# print(*dp)
print(n - 1 - idx)

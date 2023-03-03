from sys import stdin
from collections import deque


def check(a):
    if temp[a] == 0:
        return lst[a-1]
    mx = 0
    for i in d[a]:
        dummy = check(i)
        if dummy > mx:
            mx = dummy
    return mx+lst[a-1]


def topology():
    ans = []
    while stack:
        v = stack.pop()
        ans.append(v)
        for i in d[v]:
            if temp[i]:
                temp[i] -= 1
                if not temp[i]:
                    stack.append(i)
    return ans


ip = int(stdin.readline())

for _ in range(ip):
    n, k = map(int, stdin.readline().split())
    lst = list(map(int, stdin.readline().split()))
    d = [[] for _ in range(n+1)]
    temp = [0 for _ in range(n+1)]
    for i in range(k):
        a, b = map(int, stdin.readline().split())
        d[a].append(b)
        temp[b] += 1
    stack = deque()
    for i in range(1, n+1):
        if temp[i] == 0:
            stack.append(i)
    order = topology()
    dp = [0 for _ in range(n+1)]
    for i in order:
        dp[i] += lst[i-1]
        for j in d[i]:
            dp[j] = max(dp[i], dp[j])
    target = int(stdin.readline())
    print(dp[target])

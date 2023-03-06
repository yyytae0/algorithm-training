def check(a, cnt):
    global d, mx, mn
    if cnt == n:
        if d > mx:
            mx = d
        if d < mn:
            mn = d
        return

    for i in range(10):
        if lst[cnt] == '<' and not visit[i] and a < i:
            d = 10*d + i
            visit[i] = 1
            check(i, cnt+1)
            visit[i] = 0
            d = d//10
        elif lst[cnt] == '>' and not visit[i] and a > i:
            d = 10 * d + i
            visit[i] = 1
            check(i, cnt + 1)
            visit[i] = 0
            d = d // 10


n = int(input())
lst = list(input().split())
visit = [0 for _ in range(10)]
mx = 0
mn = 9999999999
for i in range(10):
    d = i
    visit[i] = 1
    check(i, 0)
    visit[i] = 0
mx, mn = str(mx), str(mn)
while len(mx) < n+1:
    mx = '0' + mx
while len(mn) < n+1:
    mn = '0' + mn
print(mx)
print(mn)

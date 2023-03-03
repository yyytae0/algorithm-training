def check():
    for i in range(n):
        team[i] = True
        find(i, 0)
        team[i] = False


def find(a, cnt):
    global mn
    if cnt == n//2-1:
        ans = solve()
        if ans < mn:
            mn = ans
        return

    for i in range(a+1, n):
        team[i] = True
        find(i, cnt+1)
        team[i] = False


def solve():
    a, b = 0, 0
    for i in range(n):
        for j in range(i+1, n):
            if team[i] and team[j]:
                a += lst[i][j] + lst[j][i]
            if not team[i] and not team[j]:
                b += lst[i][j] + lst[j][i]
    return abs(a-b)


n = int(input())
lst = list(list(map(int, input().split())) for _ in range(n))
total = 0
team = [False for _ in range(n)]
for i in range(n):
    for j in range(n):
        total += lst[i][j]
mn = 10**6
check()
print(mn)

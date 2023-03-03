from sys import stdin, setrecursionlimit


def check(b, idx):
    if idx == n:
        return

    global d
    a = lst[idx].index(b)
    b = index[a]
    if 5 <= lst[idx][a] <= 6 and 5 <= lst[idx][b] <= 6:
        d += 4
    elif lst[idx][a] == 6 or lst[idx][b] == 6:
        d += 5
    else:
        d += 6

    check(lst[idx][b], idx+1)


setrecursionlimit(10**5)
index = [5, 3, 4, 1, 2, 0]
n = int(stdin.readline())
lst = list(list(map(int, stdin.readline().split())) for _ in range(n))
ans = 0
for i in range(1, 7):
    d = 0
    check(i, 0)
    if d > ans:
        ans = d
print(ans)

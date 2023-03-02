from sys import stdin, stdout, setrecursionlimit


def check(a):
    if a == head[a]:
        return a
    head[a] = check(head[a])
    return head[a]


def union(a, b):
    a = check(a)
    b = check(b)
    if a < b:
        head[b] = a
    else:
        head[a] = b


setrecursionlimit(10**5)
n, m = map(int, stdin.readline().split())
head = [i for i in range(n+1)]
for i in range(m):
    code, n1, n2 = map(int, stdin.readline().split())
    if code:
        if check(n1) == check(n2):
            stdout.write('YES\n')
        else:
            stdout.write('NO\n')
    else:
        union(n1, n2)

# 63% 시간초과

from sys import stdin


def check(a, b):
    if head[a] == head[b]:
        return 'YES'
    return 'NO'


def add(a, b):
    if head[b] == b:
        if head[a] == a:
            head[b] = a
        else:
            head[b] = head[a]
    else:
        if head[a] == a:
            head[a] = head[b]
        else:
            if head[a] < head[b]:
                now = head[b]
                d = head[a]
                for i in s:
                    if head[i] == now:
                        head[i] = d
            else:
                now = head[a]
                d = head[b]
                for i in s:
                    if head[i] == now:
                        head[i] = d


n, m = map(int, input().split())
lst = list(list(map(int, stdin.readline().split())) for _ in range(m))
head = [i for i in range(n+1)]
s = set()
for i in lst:
    s = s|{i[1], i[2]}
    if i[0]:
        print(check(i[1], i[2]))
    else:
        add(min(i[1], i[2]), max(i[1], i[2]))

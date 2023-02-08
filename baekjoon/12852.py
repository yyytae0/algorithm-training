from collections import deque


def bfs():
    q = deque()
    q.append([n, 0])
    dct[n] = [n]
    while q:
        v = q.popleft()
        lst_v = [v[0]-1]
        if v[0] % 3 == 0:
            lst_v.append(v[0]//3)
        if v[0] % 2 == 0:
            lst_v.append(v[0]//2)

        for i in lst_v:
            if not visit[i] and 0 < i:
                q.append([i, v[1]+1])
                visit[i] = 1
                dct[i] = dct[v[0]] + [i]
                if i == 1:
                    return v[1]+1


n = int(input())
if n == 1:
    print(0)
    print(1)

else:
    visit = [0 for _ in range(n + 1)]
    dct = dict()
    print(bfs())
    print(*dct[1])

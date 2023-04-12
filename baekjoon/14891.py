from collections import deque


def make():
    lst = [[0 for _ in range(4)] for _ in range(4)]
    ar = (2 - dr[0]) % 8
    bl = (6 - dr[1]) % 8
    br = (2 - dr[1]) % 8
    cl = (6 - dr[2]) % 8
    cr = (2 - dr[2]) % 8
    dl = (6 - dr[3]) % 8
    if a[ar] != b[bl]:
        lst[0][1] = 1
        lst[1][0] = 1
    if b[br] != c[cl]:
        lst[1][2] = 1
        lst[2][1] = 1
    if c[cr] != d[dl]:
        lst[2][3] = 1
        lst[3][2] = 1
    return lst


def move(t, way):
    q = deque()
    q.append([t, way])
    visit = [0, 0, 0, 0]
    visit[t] = 1
    lst = make()
    dr[t] += way
    while q:
        v = q.popleft()
        for i in range(4):
            if lst[v[0]][i] and not visit[i]:
                nv = [i, change[v[1]]]
                visit[i] = 1
                dr[i] += nv[1]
                q.append(nv)


a = list(map(int, input()))
b = list(map(int, input()))
c = list(map(int, input()))
d = list(map(int, input()))
dr = [0, 0, 0, 0]
change = [0, -1, 1]
n = int(input())
for i in range(n):
    e, f = map(int, input().split())
    move(e-1, f)
print(a[-dr[0]%8]+b[-dr[1]%8]*2+c[-dr[2]%8]*4+d[-dr[3]%8]*8)


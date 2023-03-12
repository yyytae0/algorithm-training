def check():
    for i in range(n):
        dummy1 = 0
        dummy2 = 0
        for j in range(n):
            if lst[i][j] == 'o':
                dummy1 += 1
            else:
                dummy1 = 0
            if dummy1 >= 5:
                return True
        for j in range(n):
            if lst[j][i] == 'o':
                dummy2 += 1
            else:
                dummy2 = 0
            if dummy2 >= 5:
                return True
    return False


def bfs1(a, b):
    way = [1, 1]
    q = list()
    q.append([a, b, 1])
    while q:
        v = q[0]
        del q[0]
        v0 = v[0]+way[0]
        v1 = v[1]+way[1]
        if 0 <= v0 <= n-1 and 0 <= v1 <= n-1 and lst[v0][v1] == 'o':
            q.append([v0, v1, v[2]+1])
            if v[2]+1 == 5:
                return True


def bfs2(a, b):
    way = [1, -1]
    q = list()
    q.append([a, b, 1])
    while q:
        v = q[0]
        del q[0]
        v0 = v[0]+way[0]
        v1 = v[1]+way[1]
        if 0 <= v0 <= n-1 and 0 <= v1 <= n-1 and lst[v0][v1] == 'o':
            q.append([v0, v1, v[2]+1])
            if v[2]+1 == 5:
                return True


def cross():
    for i in range(n):
        for j in range(n):
            if lst[i][j] == 'o':
                b = bfs1(i, j)
                c = bfs2(i, j)
                if b or c:
                    return True
    return False


ip = int(input())

for case in range(1, ip+1):
    n = int(input())
    lst = list(list(input()) for _ in range(n))
    a = check()
    b = cross()
    if a or b:
        print(f'#{case} YES')
    else:
        print(f'#{case} NO')

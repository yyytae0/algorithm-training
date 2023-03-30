from collections import deque


def bfs(x, y):
    global st
    way = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    q = deque()
    q.append([x, y, lst[x][y], 1])
    while q:
        v = q.popleft()
        if v[3] == 7:
            st = st.union({v[2]})
            continue
        for i in way:
            nv = [v[0]+i[0], v[1]+i[1], v[2]*10, v[3]+1]
            if 0 <= nv[0] < 4 and 0 <= nv[1] < 4:
                nv[2] += lst[nv[0]][nv[1]]
                q.append(nv)


ip = int(input())

for case in range(1, ip+1):
    st = set()
    lst = list(list(map(int, input().split())) for _ in range(4))
    for i in range(4):
        for j in range(4):
            bfs(i, j)
    ans = len(st)
    print(f'#{case} {ans}')

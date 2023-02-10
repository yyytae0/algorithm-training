from sys import stdin


n, m = map(int, input().split())
lst = list(list(map(int, stdin.readline().split())) for _ in range(m))
visit = [0 for _ in range(n+1)]
dct = dict()
for i in lst:
    if i[0] == 0:
        if visit[i[1]]:
            if visit[i[2]]:
                dct[i[1]] = dct[i[2]] = dct[i[1]] + dct[i[2]]
            else:
                dct[i[1]].append(i[2])
                dct[i[2]] = visit[i[1]]
                visit[i[2]] = 1

        else:
            if visit[i[2]]:
                dct[i[2]].append(i[1])
                dct[i[1]] = visit[i[2]]
                visit[i[1]] = 1

            else:
                dct[i[1]] = [i[1], i[2]]
                dct[i[2]] = dct[i[1]]
                visit[i[2]] = 1
                visit[i[1]] = 1
    else:
        if not visit[i[1]] or not visit[i[2]]:
            print('NO')
        elif i[2] in dct[i[1]]:
            print('YES')
        else:
            print('NO')


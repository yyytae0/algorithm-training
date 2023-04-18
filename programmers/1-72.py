def find_s(park):
    for y, i in enumerate(park):
        for x, j in enumerate(i):
            if j == 'S':
                return [y, x]


def solution(park, routes):
    now = find_s(park)
    n = len(park)
    m = len(park[0])
    dct = {'E':[0, 1], 'S':[1, 0], 'W':[0, -1], 'N':[-1, 0]}
    for i in routes:
        dr = dct[i[0]]
        new = [now[0]+dr[0]*int(i[-1]), now[1]+dr[1]*int(i[-1])]
        if 0 <= new[0] < n and 0 <= new[1] < m and park[new[0]][new[1]] != 'X':
            for j in range(1, int(i[-1])):
                if park[now[0]+dr[0]*j][now[1]+dr[1]*j] == 'X':
                    break
            else:
                now = new
    return now

def check(db, i):
    a, b, c, d = map(int, i)
    a, b, c, d = a-1, b-1, c-1, d-1
    ni, nj = a, b
    dr = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    dr_cnt = 0
    mn = db[ni][nj]
    dummy2 = db[ni][nj]
    while True:
        dummy = dummy2
        ni, nj = ni + dr[dr_cnt][0], nj + dr[dr_cnt][1]
        if not (a <= ni <= c and b <= nj <= d):
            ni, nj = ni - dr[dr_cnt][0], nj - dr[dr_cnt][1]
            dr_cnt += 1
            ni, nj = ni + dr[dr_cnt][0], nj + dr[dr_cnt][1]
        dummy2 = db[ni][nj]
        db[ni][nj] = dummy
        if db[ni][nj] < mn:
            mn = db[ni][nj]
        if ni == a and nj == b:
            break
    return mn


def solution(rows, columns, queries):
    answer = []
    d = [[0 for _ in range(columns)] for _ in range(rows)]
    a = 1
    for i in range(rows):
        for j in range(columns):
            d[i][j] = a
            a += 1
    for i in queries:
        answer.append(check(d, i))
    # answer.sort()
    return answer


print(solution(6, 6, [[2,2,5,4],[3,3,6,6],[5,1,6,3]]))
print(solution(3, 3, [[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]]))
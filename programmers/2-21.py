way = [[0, 1], [0, -1], [1, 0], [-1, 0]]
answer = 10**6


def dfs(v, n, visit, board):
    global answer
    if v[0] == n-1 and v[1] == n-1:
        if v[3] < answer:
            answer = v[3]
        return

    for i in way:
        nv = [v[0]+i[0], v[1]+i[1], v[2], v[3]]
        if 0 <= nv[0] < n and 0 <= nv[1] < n and not visit[nv[0]][nv[1]] and not board[nv[0]][nv[1]]:
            if v[2] == i:
                nv[3] += 100
            else:
                nv[2] = i
                nv[3] += 600
            visit[nv[0]][nv[1]] = 1
            dfs(nv, n, visit, board)
            visit[nv[0]][nv[1]] = 0


def solution(board):
    global answer
    n = len(board)
    visit = [[0 for _ in range(n)] for _ in range(n)]
    dfs([0,0,[1, 0],0], n, visit, board)
    dfs([0,0,[0, 1],0], n, visit, board)
    return answer
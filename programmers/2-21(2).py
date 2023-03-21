def bfs(n, a, board):
    q = [a]
    v = [[0] * n for _ in range(n)]
    while q:
        i, j, dr, c = q.pop(0)

        for d, di, dj in ((0, -1, 0), (1, 1, 0), (2, 0, -1), (3, 0, 1)):
            ni, nj = i + di, j + dj
            if 0 <= ni < n and 0 <= nj < n and not board[ni][nj]:
                if dr == d:
                    cost = c + 100
                else:
                    cost = c + 600
                if v[ni][nj] == 0 or v[ni][nj] >= cost:
                    q.append((ni, nj, d, cost))
                    v[ni][nj] = cost
    return v[n - 1][n - 1]


def solution(board):
    n = len(board)
    ans = min(bfs(n, (0, 0, 1, 0), board), bfs(n, (0, 0, 3, 0), board))
    return ans
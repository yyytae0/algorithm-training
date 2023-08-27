def move(t):
    new_step = [[float("inf") for _ in range(5)] for _ in range(5)]
    for i in range(5):
        d = min(step[t][i], step[0][i], step[1][i], step[2][i], step[3][i], step[4][i])
        new_step[t][i] = 0
        new_step[i][t] = 0




lst = list(map(int, input().split()))
step = [[float("inf") for _ in range(5)] for _ in range(5)]
step[0][0] = 0

for i in lst:
    move()
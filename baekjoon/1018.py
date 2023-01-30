def check(x, y, lst):
    chess = ['WBWBWBWB', 'BWBWBWBW']
    cnt = 0
    change = 0
    for i in range(x, x+8):
        idx = 0
        for j in range(y, y+8):
            if lst[i][j] != chess[cnt][idx]:
                change += 1
            idx += 1
        cnt = 1 - cnt

    return min(64-change, change)


n, m = map(int, input().split())
lst = list()
for i in range(n):
    lst.append(list(input()))

ans_min = 64
for i in range(n-7):
    for j in range(m-7):
        ans = check(i, j, lst)
        if ans < ans_min:
            ans_min = ans

print(ans_min)

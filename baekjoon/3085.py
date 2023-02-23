def change(i, j):
    ans = 0
    way = [[1, 0], [0, 1]]
    for dr in way:
        ni, nj = i + dr[0], j + dr[1]
        if 0 <= ni < n and 0 <= nj < n and lst[i][j] != lst[ni][nj]:
            mx = check(i, j, ni, nj)
            if mx > ans:
                ans = mx
    return ans


def check(i, j, ni, nj):
    mx = 0
    lst[i][j], lst[ni][nj] = lst[ni][nj], lst[i][j]
    for r in [i, ni]:
        cnt = 1
        dummy = 'd'
        for d in range(n):
            if lst[r][d] == dummy:
                cnt += 1
            else:
                dummy = lst[r][d]
                if cnt > mx:
                    mx = cnt
                cnt = 1
    if cnt > mx:
        mx = cnt

    for c in [j, nj]:
        cnt = 1
        dummy = 'd'
        for d in range(n):
            if lst[d][c] == dummy:
                cnt += 1
            else:
                dummy = lst[d][c]
                if cnt > mx:
                    mx = cnt
                cnt = 1

    if cnt > mx:
        mx = cnt
    lst[i][j], lst[ni][nj] = lst[ni][nj], lst[i][j]
    return mx


n = int(input())
lst = list(list(input()) for _ in range(n))
mx = 0
for i in range(n):
    cnt = 1
    dummy = 'd'
    for j in range(n):
        if lst[i][j] == dummy:
            cnt += 1
        else:
            dummy = lst[i][j]
            if cnt > mx:
                mx = cnt
            cnt = 1
    if cnt > mx:
        mx = cnt
    cnt = 1
    dummy = 'd'
    for j in range(n):
        if lst[j][i] == dummy:
            cnt += 1
        else:
            dummy = lst[j][i]
            if cnt > mx:
                mx = cnt
            cnt = 1
    if cnt > mx:
        mx = cnt

if mx == n:
    print(n)
else:
    for i in range(n):
        for j in range(n):
            d = change(i, j)
            if d > mx:
                mx = d
    print(mx)

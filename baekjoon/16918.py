r, c, n = map(int, input().split())
lst = list(list(input()) for _ in range(r))
if n % 2 == 0:
    ans = [['O'*c] for _ in range(r)]
elif n == 1:
    ans = lst
elif n % 4 == 1:
    ans = [['O' for _ in range(c)] for _ in range(r)]
    ans2 = [['O' for _ in range(c)] for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if lst[i][j] == 'O':
                ans[i][j] = '.'
                for k in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                    if 0 <= i + k[0] < r and 0 <= j + k[1] < c:
                        ans[i + k[0]][j + k[1]] = '.'
    for i in range(r):
        for j in range(c):
            if ans[i][j] == 'O':
                ans2[i][j] = '.'
                for k in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                    if 0 <= i + k[0] < r and 0 <= j + k[1] < c:
                        ans2[i + k[0]][j + k[1]] = '.'
    ans = ans2

else:
    ans = [['O' for _ in range(c)] for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if lst[i][j] == 'O':
                ans[i][j] = '.'
                for k in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                    if 0 <= i+k[0] < r and 0 <= j+k[1] < c:
                        ans[i+k[0]][j+k[1]] = '.'

for i in ans:
    print(''.join(i))


# 반례
# 3 3 5
# OO.
# OOO
# OOO